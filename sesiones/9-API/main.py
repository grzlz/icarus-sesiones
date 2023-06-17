import requests
import pandas as pd

# Realizar la solicitud GET a la API
response = requests.get("https://jsonplaceholder.typicode.com/users")

# Verificar el código de respuesta
if response.status_code == 200:
    # Obtener los datos de la respuesta y convertirlos en un diccionario
    data = response.json()
    
    # Realizar operaciones con el diccionario
    # Por ejemplo, imprimir el contenido
else:
    print("Error al realizar la solicitud. Código de respuesta:", response.status_code)

resultados = []

for item in data:
    diccionario = {
        "name": item["name"],
        "username": item["username"],
        "city": item["address"]["city"],
        "company.name": item["company"]["name"]
    }
    resultados.append(diccionario)

df = pd.DataFrame(resultados)

print(df)