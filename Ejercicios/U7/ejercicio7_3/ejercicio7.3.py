import os

def contar_letras(fichero):
  exepciones = ['.', ' ']
  letras = fichero.readline(1)
  contador = 1
  while letras != '':
    letras = fichero.readline(1)
    if letras not in exepciones:
      contador += 1
  print(f'El archivo tiene {contador} palabras')

def contar_palabras(fichero):
  texto = fichero.read()
  texto = texto.replace('\n', '')
  texto = texto.split(' ')
  texto.pop(texto.index('.'))
  print(f'El archivo tiene {len(texto)} palabras')



path = os.path.abspath(os.path.dirname(__file__))
try:
  fichero = open(path+'/archivo.txt', 'r')
  contar_letras(fichero)
  fichero.seek(0)
  contar_palabras(fichero)
  fichero.close()
  
  
except Exception as error:
  print(f'Error: {error}. El archivo no existe')