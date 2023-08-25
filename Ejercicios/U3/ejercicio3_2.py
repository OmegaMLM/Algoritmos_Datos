'''
Ejercicio 3.2
Agencia de autos:

El programa cuenta con tres marcas de autos y su precio.

El programa debe:

pedir al usuario que ingrese la cant de dinero que dispone.
verificar que la cantidad ingresada sea un numero y sino mostrar error
verificar la cantidad de ingresada e indicar que auto o autos puede comprar
'''

# init
dinero = None
mercedez = 10000
renault = 5000
ferrari = 20000

# Input/Proceso/Out
try:
    dinero = float(input('Ingrese la cantidad de dinero que dispone: '))
    if dinero < mercedez:
        print('No se puede comprar el mercedez')
    else:
        print('Es posible comprar el mercedez')

    if dinero < renault:
        print('No se puede comprar el renault')
    else:
        print('Es posible comprar el renault')

    if dinero < ferrari:
        print('No se puede comprar el ferrari')
    else:
        print('Es posible comprar el ferrari')

except Exception as e:
    print(f'Error: {e}')
