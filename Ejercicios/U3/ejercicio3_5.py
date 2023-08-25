'''
Ejercicio 3.5
El programa debe :

Pedir al usuario un string
Determinar si esa cadena esta en minusculas o mayusculas
'''

# init
cadena = None

# input
cadena = input("Ingrese una cadena: ")

# logic
if cadena.isupper():
    print("Esta cadena esta en mayusculas")

elif not cadena.islower() and not cadena.isupper():
    print("Esta cadena esta en minusculas y en mayusculas")

else:
    print("Esta cadena esta en minusculas")
