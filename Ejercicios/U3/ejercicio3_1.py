'''Ejercicio 3.1
El programa debe:

pedir el ingreso de un número positivo al usuario y almacenar la respuesta en la variable numero.
Verificar que se trate de un numero entero y mostrar un error
Comprobar si el número es negativo. Si lo es, el programa debe avisar que no era eso lo que se había pedido. (si no hay error)
Finalmente imprimir siempre el valor introducido por el usuario.(si no hay error)
'''

# init
num = None

# Input/Process/Output
try:
    num = int(input('Ingrese el numero: '))
    if num > 0:
        print(f'El numero ingresado es: {num}')
    else:
        print(f'El numero ingresado es negativo')
except Exception as error:
    print(f'Error: {error}')
