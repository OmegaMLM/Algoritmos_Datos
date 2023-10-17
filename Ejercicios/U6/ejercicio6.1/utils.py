class Persona:
  def __init__(self, nombre='', apellido='', edad=0, ciudad=''):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.ciudad = ciudad
    
    
  
  def tipo_edad(self):
    if 0 <= self.edad < 14:
      print(f'{self.nombre} es un niño')
    elif 14 <= self.edad < 22:
      print(f'{self.nombre} es un adolecente')
    elif 22 <= self.edad < 30:
      print(f'{self.nombre} es joven')
    elif 30 <= self.edad < 50:
      print(f'{self.nombre} es mayor')
    else:
      print(f'{self.nombre} es anciano')


def add_info(self):
  self.nombre = input('Ingrese el nombre de la persona: ')
  self.apellido = input('Ingrese el apellido de la persona: ')
  self.edad = int(input('Ingrese la edad de la persona: '))
  self.ciudad = input('Ingrese la ciudad de la persona: ')
persona1 = Persona()
persona1.add_info()

