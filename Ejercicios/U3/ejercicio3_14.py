'''
Ejercicio 3.13 (Tarea)
El programa debe:

pedir un dato numerico al usuario
imprimir la tabla del numero de 1 al 10
no deben aparecer errores.
'''

#init
numero = 0
correct = True
contador = 0

#input/Process
while correct:
  try:
    numero = int(input("Ingrese un numero: "))
    correct = False
    while contador <= 10:
      print(f'{numero} X {contador} = {contador * numero}')
      contador += 1
  except Exception as error:
    print(f'Error: {error}. Ingrese un numero valido.')