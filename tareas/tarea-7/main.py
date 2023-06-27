import requests
import pandas as pd

#https://pokeapi.co/api/v2/
#https://jsonplaceholder.typicode.com/posts'
#https://api.covidtracking.com
#https://api.usaspending.gov/api/v2/agency/012/
#https://datos.gob.mx/contratacionesabiertas/

response = requests.get("https://pokeapi.co/api/v2/")
print('Status Code:', response.status_code)
print ("Headers:")
for header, value in response.headers.items():
    print(header + ":", value)