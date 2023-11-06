import os

path = os.path.abspath(os.path.dirname(__file__))
try:
  fichero = open(path+'/archivo.txt', 'r')
  palabra = input('Introduce una palabra a encontrar: ')
  completo = fichero.read()

  print(f'El archivo dice: {completo}')
  completo = completo.replace ('\n', '').replace('.', '')
  completo_spliteado = completo.split(' ')
  print(completo_spliteado)
  if palabra in completo_spliteado:
    print(f'La palabra {palabra} se encuentra en el archivo')
  else:
    print(f'La palabra {palabra} no se encuentra en el archivo')

  fichero.close()
  
except Exception as error:
  print(f'Error: {error}. El archivo no existe')