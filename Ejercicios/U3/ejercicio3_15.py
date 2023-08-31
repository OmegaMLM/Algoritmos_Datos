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
correcto = True

#Process
palabra = input('Ingrese una palabra: ')

while correcto:
  if palabra == palabra_clave:
      print('Correcto')
      correcto = False
  else:
      print('Incorrecto')
      palabra = input('Ingrese una palabra: ')

