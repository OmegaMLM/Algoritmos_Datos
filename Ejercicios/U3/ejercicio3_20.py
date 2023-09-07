'''
Ejercicio 3.20
El programa debe:

Pedir al usuario una cantidad de tramos de un viaje
pedir al usuario la duracion en minutos de cada tramo
calcular el tiempo total de viaje
no deben generar errores
'''

#Init
tramos = None
duracion = None
total = 0

#Procesos
try:
  tramos = int(input('Ingrese la cantidad de tramos: '))
  for i in range(0, tramos):
    duracion = float(input('Ingrese los minutos del tramo: '))
    total += duracion
  print(f'La duracion es de: {round(total, 2)}')
  
except Exception as error:
  print(f'Error{error}')