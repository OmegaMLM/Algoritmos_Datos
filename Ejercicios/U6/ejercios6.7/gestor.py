"""   Contar con 6 funciones disponibles en el menu **(estas funciones deben estar incluidas en una clase llamada GestorZoologico)**:

    1. Crear instancias de animales (se puede elegir entre los tres sectores) y guardarlos en una lista
    2. Crear instancia de Empleados y guardarlos en una lista
        - Los empleados se les pueden asignar animales luego, los animales al crearlos en el sistema tienen q contar siosi con un encargado
    3. Asignar a un empleado un animal a cuidar
    4. Cambiar de encargado un animal
    5. imprmiir lista de animales (con toda su informacions)
    6. imprimir lista de Empleados (con toda su informacions)

-   Se deben crear los metodos correspondientes para las funciones del menu en las clases correspondientes
-   Gestionar posibles errores
-   Estructurar el programa a criterio propio
"""
from clases import *


class GestorZoologico:
    def __init__(self):
      self.listanimales : list[Animales]= [] 
      self.listencargados : list[Encargado] = []
      
      
    def crear_animal(self):
      nombre = pedir_str('Ingrese el nombre del animal: ')
      fecha_nacimiento = validar_encargado()
      encargado_cuidar = pedir_str('Ingrese el encargado de cuidar: ')
      tipo_animal = self.validar_animal()
      animal = tipo_animal(nombre, tipo_animal, fecha_nacimiento, encargado_cuidar)

      
    def crear_encargado(self):
      legajo = pedir_int('Ingrese el legajo del encargado: ')
      nombre = pedir_str('Ingrese el nombre del encargado: ')
      apellido = pedir_str('Ingrese el apellido del encargado: ')
      empleado = Encargado(legajo, nombre, apellido)
      self.listencargados.append(empleado)
      
      
    def validar_encargado(self):
      while True:
        pedir_int('Ingrese el legajo del encargado: ')
        for encargado in self.listencargados:
          if encargado.legajo == legajo:
            return encargado
        
        
      
      
    def validar_animal(self):
      tipos_animales = {
        "animales de agua": AnimalesAgua,
        "animales de jaula": AnimalesJaula,
        "animales sueltos": AnimalesSueltos
      }
      print("Tipos de animales")
      for i in tipos_animales:
        print(i)
      tipo_animal = pedir_str("Ingrese el tipo de animal: ")
      if tipo_animal in tipos_animales:
        tipo_animal = tipos_animelas.get(tipo_animal)
        print(tipo_animal)
        return tipo_animal
        
        
    def asignar_animal(self):
      pass
    
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
        
        
gestor = GestorZoologico()
gestor.validar_animal()