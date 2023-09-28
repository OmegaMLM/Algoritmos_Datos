from prettytable import PrettyTable

"""
##**Ejercicio 5.8 (Empresa de Taxis)**
El programa debe:
*   Simular una empresa de taxis que cuente con tres Autos con sus respectivos cheferes
```
Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]
```
    *  Cada auto cuenta con un chofer y no hace recorridos mayores a lo q se le indica
*   Contar con 6 funciones disponibles en el menu:
    1. Preguntar al usuario el recorrido del viaje e indicar posibles autos y choferes
    2. Modificar nombre chofer segun el nombre del auto.
        auto_1 -> "federico"
    3. Modificar el recorrido segun el nombre del auto.
        auto_1 -> 60
    4. Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo -> ULTIMO
    5. Observar una lista de autos choferes y recorrido maximo con el siguiente formato:
    6. Observar informacion de un chofer, verificando su existencia previamente

```
AUTO    -    CHOFER    -   RECORRIDO
auto_1  -   chofer_1   -   45
auto_2  -   chofer_1   -   50
```
    
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
"""

taxis = [["IOS-124","LOS-351","IWT-853"],["juan","rafael","carlos"],[45,50,30]]

def pedir_int(texto):
  while True:
    try:
      numero = int(input(f"{texto}: "))
      return numero
    except Exception as error:
      print(f"Error: {error}. Ingrese un dato valido")

def pedir_float(texto):
  while True:
    try:
      numero = float(input(f"{texto}: "))
      return numero
    except Exception as error:
      print(f"Error: {error}. Ingrese un dato valido")        
        
def pedir_str(texto):
  string = input(f"{texto}: ")
  return string

def mostrar_taxis():
  table = PrettyTable()
  table.add_column('Auto', taxis[0])
  table.add_column('Chofer', taxis[1])
  table.add_column('Recorrido', taxis[2])
  print(table)
  

def recorrido_auto():
  recorrido = pedir_float('Introduzca el recorrido del auto')
  for i in range(len(taxis[2])):
    if recorrido >= taxis[2][i]:
      print(f'Posible auto {taxis[0][i]} con chofer {taxis[1][i]}')
    elif recorrido < taxis[2][i] and i == len(taxis[2]) - 1:
      print('No hay autos con ese recorrido')
      
def mod_nombre_auto():
  nombre_auto = pedir_str('Introduzca el nombre del auto').upper()
  try:
    indice = taxis[0].index(nombre_auto)
    print(f'Posible auto {taxis[0][indice]} con chofer {taxis[1][indice]}')
    nombre_chofer = pedir_str('Introduzca el nombre del chofer').lower()
    taxis[1][indice] = nombre_chofer
  
  except:
    print('No existe el auto')
    
    
def mod_recorrido_auto():
  nombre_auto = pedir_str('Introduzca el nombre del auto').upper()
  try:
    indice = taxis[0].index(nombre_auto)
    print(f'Posible auto {taxis[0][indice]} con recorrido {taxis[2][indice]}')
    recorrido = pedir_str('Introduzca el recorrido').lower()
    taxis[2][indice] = recorrido
  
  except:
    print('No existe el auto')
    
def add_auto():
  nombre_auto = pedir_str('Introduzca el nombre del auto').upper()
  nombre_chofer = pedir_str('Introduzca el nombre del chofer')
  recorrido = pedir_float('Introduzca el recorrido')
  taxis[0].append(nombre_auto)
  taxis[1].append(nombre_chofer)
  taxis[2].append(recorrido)

def info_chofer():
  nombre_chofer = pedir_str('Introduzca el nombre del chofer').lower()
  try:
    indice = taxis[1].index(nombre_chofer)
    table = PrettyTable()
    table.field_names = ['Nombre', 'Auto', 'Recorrido']
    table.add_row([taxis[1][indice], taxis[0][indice], taxis[2][indice]])
    print(table)
  except Exception as error:
    print(f'Error: {error}. No existe el chofer')
    