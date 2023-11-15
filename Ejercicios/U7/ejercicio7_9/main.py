import os
import json

path = os.path.abspath(os.path.dirname(__file__))

fichero = open(f'{path}/estudiantes.json', 'r')
diccionario = json.load(fichero)
for estudiante in diccionario['estudiantes']:
    print(f'Nombre: {estudiante["nombre"]}')
    print(f'Edad: {estudiante["edad"]}')
    print(f'Asignaturas: {estudiante["asignaturas"]}')

fichero.close()