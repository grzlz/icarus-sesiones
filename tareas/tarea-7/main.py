import requests
import pandas as pd
import json

#https://pokeapi.co/api/v2/pokemon/ditto
#https://api.spotify.com/v1/recommendations
#https://api.covidtracking.com
#https://api.usaspending.gov/api/v2/agency/012/
#https://datos.gob.mx/contratacionesabiertas/

response1 = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
response2 = requests.get("https://api.spotify.com/v1/recommendations")
response3 = requests.get("https://api.covidtracking.com")
response4 = requests.get("https://api.usaspending.gov/api/v2/agency/012/")
response5 = requests.get("https://datos.gob.mx/contratacionesabiertas/")

lista_response = [response1,response2,response3,response4,response5]

for r in lista_response:
    print("Status Code:", r.status_code)
    print("Headers:", r.headers)



