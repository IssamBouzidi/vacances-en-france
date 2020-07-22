import json
import os
import sys
from bottle import Bottle, run, request, template, debug, static_file
import psycopg2
import back.data_access as dba
from back.config import db
import requests
from navitia_client import Client

dirname = os.path.dirname(sys.argv[0])

app = Bottle()

debug(True)

client = Client(user="ad11008a-2d53-4612-829a-00b13ad2a613")
client.set_region("sncf")

stop_area = "admin:fr:63113"
response = client.journeys(origin=stop_area, verbose=True)

print(response)


dba.db_connexion(db.connexion_string)

"""
Run server
"""
run(app, host='localhost', port=8080)
