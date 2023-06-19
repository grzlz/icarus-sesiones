import requests
import json

# replace 'your_url_here' with the actual URL you're targeting
url = 'https://jsonplaceholder.typicode.com/users'

# Send a GET request to the URL
response = requests.get(url)

# Parse the response content as JSON
data = response.json()

# The `data` variable now holds the data as a Python dictionary/list
print(data)
