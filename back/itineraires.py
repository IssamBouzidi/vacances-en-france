import requests
from navitia_client import Client
from datetime import datetime
import psycopg2
import back.data_access as dba
from back.config import db


""" recuperer les prefectures
"""
def get_prefecture():
    dba.db_connexion(db.connexion_string)
    sql_query = 'SELECT * FROM prefecture'
    result = dba.dict(sql_query, None, db.connexion_string)

    return result


"""recuperer la liste des codes insee
return:
list des codes insee
"""
def get_insee_code():
    sql_query = 'SELECT code_insee FROM prefecture'
    data = dba.dict(sql_query, None, db.connexion_string)
    result = [item[0] for item in data]
    return result


"""inserer un trajet
"""
def insert_itineraire(sql_query):
    dba.empty(sql_query, None, db.connexion_string)

def get_itineraire():
    

"""recuperer la liste des trajets
params:[
    client: object contenant les informations d'authentification de l'api sncf
    prefecture_depart: prefecture de depart
    prefecture_arrivee: prefecture d'arrivee
    datetime_depart: date de depart
]
return:
list des trajets
"""
def get_journeys(
        client,
        prefecture_depart,
        prefecture_arrivee,
        datetime_depart):

    code_insee_depart = f"admin:fr:{prefecture_depart}"
    code_insee_arrivee = f"admin:fr:{prefecture_arrivee}"

    response = client.journeys(
        origin=code_insee_depart,
        destination=code_insee_arrivee,
        datetime=datetime_depart)

    return response.json()
