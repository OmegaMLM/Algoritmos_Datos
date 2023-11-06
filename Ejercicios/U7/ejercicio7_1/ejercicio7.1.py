import os

path = os.path.abspath(os.path.dirname(__file__))
print(path)

fichero = open(path+'/archivo.txt', 'r')
linea = fichero.readline(1)
oracion = linea
while linea != '.':
  oracion += linea
  linea = fichero.readline(1)
  
    
print(oracion)
fichero.close()