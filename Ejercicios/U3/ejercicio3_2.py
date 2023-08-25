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

    if dinero >= ferrari:
        print(f'Es posible comprar todos los autos')
    elif dinero > renault and dinero < ferrari:
        print(f'Es posible comprar el mercedez y el renault')
    elif dinero >= renault < mercedez:
        print(f'Es posible comprar el renault')
    else:
        print('No es posible comprar ningun auto.')

except Exception as e:
    print(f'Error: {e}')
