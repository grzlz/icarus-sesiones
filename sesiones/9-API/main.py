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

variables_deseadas = ["name","username","address.city","company.name"]

filtered_data = []

for d in data:
    values = {}
    for key in variables_deseadas:
        keys = key.split('.')
        current_value = d
        for k in keys:
            if k in current_value:
                current_value = current_value[k]
            else:
                current_value = None
                break
        values[key] = current_value
    filtered_data.append(values)

df = pd.DataFrame(filtered_data)


print(df)