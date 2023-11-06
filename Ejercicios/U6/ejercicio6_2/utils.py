
class FiguraGeometrica:
  def __init__(self, tipo_de_figura, color, tamanio):
    self.tipo_de_figura = tipo_de_figura
    self.color = color
    self.tamanio = tamanio
    
  def presentarse(self):
    print(f'Es un {self.tipo_de_figura} de color {self.color} y tamanio {self.tamanio}')
  
  def cambiar_color(self):
    color = input('Ingrese el nuevo color: ')
    self.color = color
    print(f'El nuevo color es {self.color}')
    
  def verificar_tamaño(self):
    if self.tamanio == "pequeño":
      self.tamanio = "grande"
    print(f'La figura es {self.tamanio}')
      
def programa():
  fig = FiguraGeometrica("cuadrado", "rojo", "pequeño")
  fig.presentarse()
  fig.cambiar_color()
  fig.verificar_tamaño()
    
