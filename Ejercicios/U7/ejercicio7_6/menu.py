import os

path = os.path.abspath(os.path.dirname(__file__))

fichero = open(f'{path}/archivo.txt', 'w+')
cantidad_palabras = int(input('Introduce la cantidad de palabras: '))
for i in range(0, cantidad_palabras):
  palabra = input('Introduce una palabra: ')
  fichero.write(f'{palabra}\n')
fichero.close()

