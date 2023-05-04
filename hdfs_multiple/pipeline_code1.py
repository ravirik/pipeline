import requests

url = "http://api.example.com/data"
params = {"param1": "value1", "param2": "value2"}

response = requests.get(url, params=params)

# Do something with the response data
data = response.json()

