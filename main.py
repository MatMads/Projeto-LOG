from datetime import datetime
import requests
import json

CAMINHO_ARQUIVO = "E:\\Documentos\\Projetos\\Python\\TESTES\\Projeto-LOG\\"
hora = datetime.now()
hora = hora.strftime("%d-%m-%Y_%Hh%Mm%Ss")
print(hora)




URL_BASE = 'https://randomuser.me/api/'

response = requests.get(URL_BASE)

dados = response.json()


with open (f'{CAMINHO_ARQUIVO}{hora}.json', 'w+') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)


with open (f'{CAMINHO_ARQUIVO}{hora}.txt', 'w+', encoding='utf8') as arquivo:
    arquivo.write(str(dados))