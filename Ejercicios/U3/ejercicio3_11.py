'''
Ejercicio 3.11
El programa debe:

pedir al usuario 5 datos numericos
verificar que sean enteros y sino pedir nuevamente los 5
cuando se tenga los 5 datos el programa debe devolver el promedio
no deben aparecer errores.
'''

#init
numeros = None
no_entero = True
promedio = None
num1 = None
num2 = None
num3 = None
num4 = None
num5 = None

#Process
while no_entero:
  try:
    num1 = int(input("Ingrese el numero 1: "))
    num2 = int(input("Ingrese el numero 2: "))
    num3 = int(input("Ingrese el numero 3: "))
    num4 = int(input("Ingrese el numero 4: "))
    num5 = int(input("Ingrese el numero 5: "))
    no_entero = False
    promedio = (num1 + num2 + num3 + num4 + num5) / 5
    print(f'El promedio de los 5 numeros es: {promedio}.')
  
  #Caching error
  except ValueError:
    print("Ingrese solo numeros enteros.")
