import os


def crear_archivo(nombre_fichero):
  fichero = open(f'{path}/{nombre_fichero}', 'a+')
  return fichero
def escribir_archivo(fichero):
  cantidad_palabras = int(input('Introduce la cantidad de palabras: '))
  for i in range(0, cantidad_palabras):
      palabra = input('Introduce una palabra: ')
      fichero.write(f'{palabra}\n')
      
def leer_linea(fichero):
  fichero.seek(0)
  lineas = fichero.readlines()
  
  for i in lineas:
    i = i.replace('\n', '')
    print(i)
    input('Enter para mostrar mas lineas')
  
def  borrar_archivo(fichero):
  fichero.truncate(0)
  
path = os.path.abspath(os.path.dirname(__file__))

try:
  nombre_fichero = input('Introduce el nombre del archivo: ')
  fichero = crear_archivo(nombre_fichero)
  escribir_archivo(fichero)
  leer_linea(fichero)
  borrar_archivo(fichero)
  fichero.close()
except Exception as error:
    print(f'Error: {error}. El archivo no tiene extencion')