'''
Ejercicio 3.19
El programa debe:

Preguntar al usuario una cantidad de dinero a invertir
Preguntar al usuario el interés anual y el número de años
Mostrar por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''

#Init
try:
  invertir = float(input('Ingrese la cantidad de dinero a invertir: '))
  interes = float(input('Ingrese la cantidad de interes anual: '))
  anios = int(input('Ingrese la cantidad de anios: '))
  for i in range(0,anios):
    invertir += (invertir * interes) / 100
    
  print(f'El capital obtenido es: {round(invertir, 2)}')
except Exception as error:
  print(f'Error: {error}')