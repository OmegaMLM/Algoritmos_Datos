import os


class LectorDeArchivos:
  def __init__(self):
    self.path = os.path.abspath(os.path.dirname(__file__))
  def  abrir_archivo(self, nombre_archivo):
    try:
        self.fichero = open(f'{self.path}/{nombre_archivo}', 'r')
    except Exception as error:
        print(f'Error: {error}. El archivo no existe')
        
  def leer_archivo(self):
    texto = self.fichero.read()
    print(texto)
    self.fichero.seek(0)
    
  def cerrar_archivo(self):
    self.fichero.close()
    
  def encontrar_comas(self):
    caracter = self.fichero.readline(1)
    comas = 0
    while caracter != '':
      caracter = self.fichero.readline(1)
      if caracter == ',':
        comas += 1
    print(f'El archivo tiene {comas} comas')
    self.fichero.seek(0)
    
  def palabras_3_caracteres(self):
    palabras_3 = 0
    contenido = self.fichero.read()
    contenido = contenido.replace('\n', '')
    palabras = contenido.split(' ')
    for palabra in palabras:
      if len(palabra) == 3:
        palabras_3 += 1
    print(f'El archivo tiene {palabras_3} palabras de 3 caracteres')
    self.fichero.seek(0)
    
  def sacar_palabra(self, palabra):
    print(self.fichero.read().replace(palabra, ''))
    self.fichero.seek(0)
    
lector = LectorDeArchivos()
lector.abrir_archivo('archivo.txt')
lector.leer_archivo()
lector.encontrar_comas()
lector.palabras_3_caracteres()
lector.sacar_palabra('del')
lector.cerrar_archivo()



