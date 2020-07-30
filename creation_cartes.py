import folium
import back.data_access as dba
from back.config import db

coordinates = []

def get_trajets(type_trajet):

    sql = f"""select p_d.commune, p_a.commune, p_d.geo_point_2d, p_a.geo_point_2d, t.datetime_depart, t.datetime_arrivee, t.duree, t_t.libelle_type_trajet 
            from trajets t
            INNER JOIN prefecture p_d on t.prefecture_id_depart = p_d.id_prefecture
            INNER JOIN prefecture p_a on t.prefecture_id_arrivee = p_a.id_prefecture
            INNER JOIN type_trajet t_t on t.type_trajet_id = t_t.id_type_trajet
            where t.type_trajet_id = {type_trajet}
            order by t.datetime_depart
            """

    data = dba.dict(sql, None, db.connexion_string)
    return data

def get_itineraire(type_trajet, color):
    """recuperer le trajet le plus court
    """
    trajets = get_trajets(type_trajet)

    """remplir le tableau par les coordonées goegraphique
    """
    for trajet in trajets:
        coordinates.append(
            [
                float(trajet[2].split(',')[0]),
                float(trajet[2].split(',')[1])
                ]
            )

    """ajouter la derniere prefecture
    """
    coordinates.append(
            [
                float(trajets[len(trajets) - 1][3].split(',')[0]),
                float(trajets[len(trajets) - 1][3].split(',')[1])
                ]
            )

    """creer le point de depart dans la carte
    """
    m = folium.Map(location=[coordinates[0][0] , coordinates[0][1]], zoom_start=6)

    """ajout des point de depart et de la fin
    """
    folium.Marker([coordinates[0][0] , coordinates[0][1]], popup = trajets[0][0]).add_to(m)
    folium.Marker([coordinates[len(coordinates) - 1][0] , coordinates[len(coordinates) - 1][1]], popup=trajets[len(trajets) - 1][0]).add_to(m)

    """creer l'itineraire
    """
    aline=folium.PolyLine(locations=coordinates,weight=2,color = color)
    m.add_child(aline)

    return m

"""enregistrer le resultat sous format html
"""
get_itineraire(1, 'blue').save('chemin_plus_court.html')


"""enregistrer le resultat sous format html
"""
get_itineraire(2, 'green').save('chemin_moins_co2.html')