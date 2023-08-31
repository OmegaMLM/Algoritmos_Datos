'''
Ejercicio 3.10
El programa debe:

Pedir un numero incial al usuario
Pedir un numero limite al usuario
imprimir desde el inicio al limite
no debe generar errores
'''

num_final = None
num = None
try:
    num = int(input("Ingrese un numero inicial: "))
    num_final = int(input('Ingrese el numero final: '))
    while num <= num_final:
        print(f'Numero: {num}')
        num += 1
except Exception as e:
    print(f'Ingreso fallido. Error: {e}')
