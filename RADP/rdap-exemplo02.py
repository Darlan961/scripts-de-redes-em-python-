import requests 
import json

pfx = '<DIGITE AQUI O PREFIXO>'
url = f'https://rdap.registro.br/ip/{pfx}'

response = requests.get(url)

data_url_json = response.json() 

for key, value in data_url_json.items():
 print(key, ' = ', value)
