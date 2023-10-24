"""Crear clase GestorComputadora que cuente con las siguientes funciones para un menu
1.   Crear Computadora, indicando tipo y guardar en una lista. Verificando marca y SO de una lista
2.   Listar Computadoras (presentandolos), indicando tipo.
3.   Cambiar SO de una Computadora, verificando una lista de SO disponibles
4.   Listar perifericos
  """
from computadoras import *

class GestorComputadora:
    def __init__(self):
        self.listcomputadoras : list[Computadoras] = []
        self.marcasDisponible = ["msi", "asus", "lenovo", "acer"]
        self.soDisponible = ["windows 10", "windows 11", "ubuntu", "kali linux"]
    
    def crearComputadora(self):
        cls = self.validar_tipo()
        id_modelo = pedir_int('Escriba el id del modelo: ')
        perifericos = self.validar_perifericos()
        so = self.validar_so()
        marca = self.validar_marca()
        if cls.__name__ == 'Notebook':
            bateria = pedir_int('Elija la cantidad de bateria de la computadora: ')
            self.listcomputadoras.append(Notebook(id_modelo, perifericos, so, marca, bateria))
        elif cls.__name__ == 'Escritorio':
            grafica = pedir_str('Elija la grafica de la computadora: ')
            self.listcomputadoras.append(Escritorio(id_modelo, perifericos, so, marca, grafica))
    def listarComputadoras(self):
        for cls in self.listcomputadoras:
            cls.tipo_computadora()
            cls.presentarse()
            

    def validar_tipo(self):
      while True:
        for tipos in Computadoras.__subclasses__():
          print(tipos.__name__)
        tipo = pedir_str('Elija el tipo de computadora: ').lower().capitalize()
        for cls in Computadoras.__subclasses__():
            if cls.__name__ == tipo:
                return cls
        print("Tipo de computadora no reconocido")
        
    def validar_marca(self):
      while True:
        print(f"Marcas disponibles: {self.marcasDisponible}")
        marca = pedir_str('Elija la marca de la computadora: ').lower()
        if marca in self.marcasDisponible:
          return marca
        else:
          print("Marca no reconocida")
        
    def validar_perifericos(self):
      listperifericos = []
      numero = pedir_int('Elija la cantidad de perifericos de la computadora: ')
      for cantidad in range(numero):
        perifericos = pedir_str('Elija el periferico de la computadora: ')
        listperifericos.append(perifericos)
      return listperifericos

    def validar_so(self):
      while True:
        print(f"Sistemas operativos disponibles: {self.soDisponible}")
        so = pedir_str('Elija el SO de la computadora: ').lower()
        if so in self.soDisponible:
          return so
        else:
          print("SO no reconocida")
      
    def lista_cambiar_so(self):
      id = pedir_int('Elija el id de la computadora: ')
      for computadora in self.listcomputadoras:
        if computadora.id_modelo == id:
          so = pedir_str('Elija el SO de la computadora: ')
          computadora.cambiar_so(so)
          return computadora
      print("Computadora no encontrada")
      
    def listar_perifericos(self):
      id = pedir_int('Elija el id de la computadora: ')
      for computadora in self.listcomputadoras:
        if computadora.id_modelo == id:
          print(f"Los perifericos de la computadora son: {computadora.listaPerifericos}")
          
def pedir_str(text):
  string = input(text)
  return string

def pedir_float(text):
  while True:
    try:
      numero = float(input(text))
      return numero
    except Exception as error:
      print(f'Error: {error}. Ingrese un dato valido')

def pedir_int(text):
  while True:
    try:
      numero = int(input(text))
      return numero
    except Exception as error:
      print(f'Error: {error}. Ingrese un dato valido')
        