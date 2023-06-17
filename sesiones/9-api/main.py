import requests
import pandas as pd

response = requests.get('https://jsonplaceholder.typicode.com/users')

if response.status_code == 200:
    # La solicitud fue exitosa
    data = response.json()
else:
    # La solicitud falló
    print("Error en la solicitud:", response.status_code)

data1 = []
for i in data:
    important = {
        "name": i["name"],
        "username": i["username"],
        "city": i["address"]["city"],
        "company_name": i["company"]["name"]
    }
    data1.append(important)


df = pd.DataFrame(data1)

print(df)

