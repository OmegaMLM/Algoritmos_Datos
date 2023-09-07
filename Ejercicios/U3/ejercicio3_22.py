'''
Ejercicio 3.22
El programa debe:

Pedir al usuario cantidad de personas
pedir al usuario una a una la edad de las personas
finalizado la carga de las edades debe imprimir por pantalla la edad mayor
no deben generar errores
'''

#init 
personas = None
edad = None
mayor = 0


while True:
  try:
    personas = int(input('Ingrese la cantidad de personas: '))
    for i in range(0, personas):
      while True:
        try:
          edad = int(input(f'Ingrese la edad de la persona {i+1}: '))
          if mayor < edad:
            mayor = edad
          break
        except:
          print('Introduzca una edad valida.')
    print(f'La persona con mayor edad tiene: {mayor}')
    break
  except:
    print('Introduzca un cantidad de personas valida.')