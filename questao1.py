import requests
import sys

page = requests.get('https://servicodados.ibge.gov.br/api/v1/censos/nomes/basica?nome='+sys.argv[1]+'&sexo='+sys.argv[2])
page_json = page.json()
print(page_json[0]['nomes'])
print(page_json[0]['freq'])
