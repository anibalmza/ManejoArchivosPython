import json # https://www.analyticslane.com/2018/07/16/archivos-json-con-python/
import os

path, _ = os.path.split(os.path.abspath(__file__))

data = {} # creo un diccionario

data["empresa"] = "Python"

data['clientes'] = [] # creo la categoria clientes,
# como una lista de "Objetos" del tipo diccionarios.

data['clientes'].append({
    'nombre': 'Juan',
    'apellido': 'Perez',
    'ciudad': 'Mendoza',
    'saldo': 7518})

data['clientes'].append({
    'nombre': 'Pedro',
    'apellido': 'Sanchez',
    'ciudad': 'Cordoba',
    'saldo': [1980, 5500]})

data['clientes'].append({
    'nombre': 'Andres',
    'apellido': 'Gonzalez',
    'ciudad': 'Buenos Aires',
    'saldo': 10200})

with open(path+'/WriteData.json', 'w') as file:
    json.dump(data, file, indent=4)