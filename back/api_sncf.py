import requests
from navitia_client import Client
from datetime import datetime

client = Client(user="ad11008a-2d53-4612-829a-00b13ad2a613")
client.set_region("sncf")

def get_journeys():
    
    gare_depart = "admin:fr:63113"
    gare_arrivee = "admin:fr:69123"
    date_depart = datetime.now().strftime("%Y%m%dT%H%M%S")
    response = client.journeys(origin=gare_depart, destination = gare_arrivee, datetime = date_depart)

    print(response.json())