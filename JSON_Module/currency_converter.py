import requests
import json

response = requests.get("https://www.floatrates.com/daily/usd.json")
data = json.loads(response.text) # response.text is str object
#print(json.dumps(data, indent=2))
#print(data['try']['rate'])

for i,j in data.items():
    rate = j['rate']
    name = j['name']
    print(f'1 USD = {rate} {name}')