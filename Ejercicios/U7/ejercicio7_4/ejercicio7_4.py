import os

def buscar_titulos(fichero):
  oracion = fichero.readlines()
  titulos = []
  oracion_split = []
  for i in oracion:
    oracion_split = i.split(' ')
    titulos.append(oracion_split[0])
  print(f'Los titulos son: {titulos}')
    
def devolver_columanas(fichero):
  oracion = fichero.readlines()
  oracion_split = []
  columas = 0
  for i in oracion:
    oracion_split = i.split(' ')
    oracion_split.pop(len(oracion_split) - 1)
    if len(oracion_split) > columas:
      columas = len(oracion_split)
  print(f'La cantidad de columnas es {columas}')
  
def devolver_filas(fichero):
  print(f'La cantidad de filas es: {len(fichero.readlines())}')
    
path = os.path.abspath(os.path.dirname(__file__))
try:
  fichero = open(path+'/archivo.txt', 'r')
  buscar_titulos(fichero)
  fichero.seek(0)
  devolver_columanas(fichero)
  fichero.seek(0)
  devolver_filas(fichero)
  fichero.close()
  
except Exception as error:
  print(f'Error: {error}. El archivo no existe')