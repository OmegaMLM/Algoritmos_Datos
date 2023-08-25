'''
Ejercicio 3.3
El programa debe :

Determinar si una cadena posee sólo números (metodos de string)
'''

# init
cadena = None

# input
cadena = input("Ingrese una cadena de numero: ")
# proceso
if cadena.isnumeric():
    print("La cadena posee solo números")
else:
    print("La cadena no posee solo números o no tiene numeros")
