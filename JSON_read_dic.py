import json # https://www.analyticslane.com/2018/07/16/archivos-json-con-python/
import os

path, _ = os.path.split(os.path.abspath(__file__))

with open(path+'/WriteData.json') as file:
    data = json.load(file)

print(type(data))

for client in data['clientes']:
        print('')
        print('Nombre:', client['nombre'])
        print('Apellido:', client['apellido'])
        print('Ciudad:', client['ciudad'])
        print('Saldo $:', client['saldo'])