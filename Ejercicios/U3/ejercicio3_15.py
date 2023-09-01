'''
Ejercicio 3.15
El programa debe:

pedir un dato al usuario
solo en caso que este escriba la palabra clave "python" imprimir por pantalla "Correcto", en caso contrario debe seguir pidiendo el dato
no deben aparecer errores.
'''

#init
palabra_clave = 'python'
palabra = None

#Process

while True:
  palabra = input('Ingrese una palabra: ')
  palabra = palabra.lower()
  if palabra == palabra_clave:
      print('Correcto')
      break
  else:
      print('Incorrecto')

