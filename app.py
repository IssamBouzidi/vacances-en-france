import json
import os
import sys
from bottle import Bottle, run, request, template, debug, static_file
import psycopg2
import back.data_access as dba
from back.config import db
import requests
from navitia_client import Client
from datetime import datetime
import back.itineraires as itineraires
import folium

"""Table qui contient la liste des code INSEE
    """
list_code_insee = []

"""api keys pour recupere les données de l'api SNCF
    """
user_1 = "ed4e0720-a576-4ecf-b090-fe60197dc4d9"
user_2 = "df326fe0-de2e-4c20-884c-452c4ca87326"
user_3 = "67031fc9-1e84-4f66-ba94-8f93fe319945"

"""initialisation du serveur
    """
dirname = os.path.dirname(sys.argv[0])
app = Bottle()
debug(True)

"""fonction permettant de recuperer un itineraire
    """


def get_itineraire():
    """recuperer la liste des codes INSEE
    """
    list_code_insee = itineraires.get_insee_code()

    """initialisation de la prefecture de depart et de la date de depart
    """
    code_insee_depart = '63113'
    date_depart = datetime(2020, 8, 1, 5, 0, 0, 0).strftime("%Y%m%dT%H%M%S")

    """recuperer les trajets liés un un itinieraire
    """
    get_trajet(list_code_insee, code_insee_depart, date_depart)

    """fonction permettant de recuperer les trajets
    params:[
        list_insee: tabeau contenant liste des codes insee
        prefecture_depart: la prefecture de depart
        date_depart: date du depart
        index: permet d'alterner sur les api sncf
    ]
    """


def get_trajet(list_insee, prefecture_depart, date_depart, index=0, type_trajet_id = 1, itineraire_id = 1):
    """initialisation des variables
    """
    duree_min = 86400
    prefecture_arrivee = None
    datetime_arrivee = None
    datetime_depart = None
    trajet_trouvee = False
    taux_co2 = 9999999999

    """choix de la clé api à utiliser
    """
    if (index % 3) == 0:
        client = Client(user=user_1)
    if (index % 3) == 1:
        client = Client(user=user_2)
    if (index % 3) == 2:
        client = Client(user=user_3)
    client.set_region("sncf")

    index += 1

    """supprimer la prefecture de depart pour ce trajet
    """
    list_insee.remove(prefecture_depart)

    try:

        for code_insee_arrivee in list_insee:
            """récuperer les trajets d'une prefecture de depart vers une prefecture d'arriver
            """
            journeys = itineraires.get_journeys(
                client, prefecture_depart, code_insee_arrivee, date_depart)

            """si un trajet existe
            """
            if "journeys" in journeys:
                for journey in journeys['journeys']:

                    """calculer le delai d'attente dans la gare
                    """
                    duree_attente = datetime.strptime(
                        journey['departure_date_time'],
                        '%Y%m%dT%H%M%S') - datetime.strptime(
                        date_depart,
                        '%Y%m%dT%H%M%S')
                    """calculer la duree du trajet delai d'attente inclus
                    """
                    duree_trajet = int(duree_attente.seconds) + \
                        int(journey['duration'])

                    """tester quel itineraire on calcul, plus court ou moins emetteur de co2
                    """
                    if(type_trajet_id == 1 and duree_trajet <= duree_min) or (type_trajet_id == 2 and journey['co2_emission']['value'] <= taux_co2):
                        duree_min = int(duree_trajet)  # journey['duration']
                        prefecture_arrivee = code_insee_arrivee
                        datetime_arrivee = journey['arrival_date_time']
                        datetime_depart = journey['departure_date_time']
                        taux_co2 = journey['co2_emission']['value']
                        trajet_trouvee = True

        """si un trajet court ou moins emetteur de co2 a été trouvé
        """
        if trajet_trouvee:
            sql = f"""insert into trajets
            (prefecture_id_depart, prefecture_id_arrivee, datetime_depart, datetime_arrivee, taux_co2, duree, type_trajet_id, itineraire_id) values(
            (select id_prefecture from prefecture where code_insee like '{prefecture_depart}'),
            (select id_prefecture from prefecture where code_insee like '{prefecture_arrivee}'),
            '{datetime_depart}', '{datetime_arrivee}', {taux_co2}, {duree_min}, {type_trajet_id}, {itineraire_id})"""

            """stocker le trajet dans la base de données
            """
            itineraires.insert_itineraire(sql)
        else:
            print("Aucun trajet trouvee")

        """si on encore des prefecture non encore visitées
            on appel la fonction avec les params suivant
            params:[
                list_insee: liste des codes insee restants
                prefecture_arrivee: prefecture arrivee qui deviendra prefecture de depart pour rechercher le trajet suivant
                datetime_arrivee: date d'arrive qui deviendra la date de depart pour le trajet suivant
                index: permet d'alterner sur les api sncf
            ]
        """
        if len(list_insee) > 0:
            get_trajet(list_insee, prefecture_arrivee, datetime_arrivee, index)

    except Exception as ex:
        print(f"Error: {ex}")

"""fonction main du programme
"""
if __name__ == "__main__":
    """appel de la fonction get irineraire
    """
    get_itineraire()