class Persona:
  def __init__(self, nombre='', apellido='', edad=0, ciudad=''):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.ciudad = ciudad
    
  def description(self):
    return f'Soy {self.nombre} {self.apellido}, tengo {self.edad} años y vivo en {self.ciudad}'
  
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

def inicio():
  persona1 = Persona(input('Nombre: '), input('Apellido: '), int(input('Edad: ')), input('Ciudad: '))
  print(persona1.description())
  persona1.tipo_edad()
  
  