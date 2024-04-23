
import requests 
import json

asn = '<DIGITE O ASN AQUI>'
url = f'https://rdap.registro.br/autnum/{asn}'

response = requests.get(url)

data_url_json = response.json() 

for key, value in data_url_json.items():
 print(key, ' = ', value)