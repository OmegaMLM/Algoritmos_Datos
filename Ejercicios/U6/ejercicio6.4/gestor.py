"""Crear clase GestorAutos que cuente con las siguientes funciones para un menu

1.  Crear auto, indicando tipo de auto y guardar en una lista
2.  Listar autos (presentandolos), indicando tipo de Vehiculo.
3.  Cambiar velocidad de un Vehiculo
4.  Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)

"""
from autos import *


class GestorAutos:
  def __init__(self):
    self.list_vehiculos : list[Vehiculo] = []
    
  def crear_vehiculo(self):
    for i in Vehiculos.__subclasses__():
      print(i.__name__)
    tipo_de_vehiculo = self.verificar_tipo_vehiculo()
    patente = pedir_str('Ingrese la patente: ').upper()
    marca = pedir_str('Ingrese la marca: ').lower().capitalize()
    anio = pedir_int('Ingrese el anio: ')
    origen = pedir_str('Ingrese el origen: ').lower().capitalize()
    
    match tipo_de_vehiculo.__name__:
      case 'Deportivo':
        deportivo = Deportivo(patente, marca, anio, origen, pedir_float('Ingrese el torque: '))
        self.list_vehiculos.append(deportivo)
      case 'Particular':
        particular = Particular(patente, marca, anio, origen, pedir_int('Ingrese el asientos: '))
        self.list_vehiculos.append(particular)
      case 'Pickup':
        pickup = Pickup(patente, marca, anio, origen, pedir_float('Ingrese la carga: '))
        self.list_vehiculos.append(pickup)
      case _:
        print('Tipo de vehiculo no reconocido')
  def presentar_todos(self):
    for todos in self.list_vehiculos:
      print(f'Vehiculo: {todos.__class__.__name__}')
      Vehiculos.mostrar_info(todos)
      
  def verificar_tipo_vehiculo(self):
    while True:
      tipo_de_vehiculo = pedir_str('Ingrese el tipo de vehiculo: ').lower().capitalize()
      for cls in Vehiculos.__subclasses__():
          if cls.__name__ == tipo_de_vehiculo:
              print(f'El tipo de vehiculo elegido es: {cls.__name__}')
              return cls
      print("Tipo de vehiculo no reconocido")
      
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

def cambiar_velocidad(self):
  patente = pedir_str("Ingrese la patente del vehiculo que desea cambiar la velocidad: ")
  for auto in self.list_vehiculos:
    if auto.patente == patente:
      velocidad = pedir_float("Ingrese la nueva velocidad: ")
      tipo = auto.__class__.__name__
      auto.velocidad = tipo.setear_velocidad(velocidad) 

obj_gestor = GestorAutos()

obj_gestor.crear_vehiculo()
obj_gestor.crear_vehiculo()

obj_gestor.presentar_todos()

