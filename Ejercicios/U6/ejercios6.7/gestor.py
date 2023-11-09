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
      fecha_nacimiento = pedir_str('Ingrese la fecha de nacimiento (dd/mm/aaaa): ')
      encargado_cuidar =  self.validar_encargado()
      tipo_animal = self.validar_animal()
      animal = tipo_animal(nombre, tipo_animal, fecha_nacimiento, encargado_cuidar)
      self.listanimales.append(animal)

      
    def crear_encargado(self):
      legajo = pedir_int('Ingrese el legajo del encargado: ')
      nombre = pedir_str('Ingrese el nombre del encargado: ')
      apellido = pedir_str('Ingrese el apellido del encargado: ')
      empleado = Encargado(legajo, nombre, apellido)
      self.listencargados.append(empleado)
      
      
    def validar_encargado(self):
      while True:
        legajo = pedir_int('Ingrese el legajo del encargado: ')
        for encargado in self.listencargados:
          if encargado.legajo == legajo:
            return encargado
          print('Encargado no encontrado')
          return -1
        
      
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
        tipo_animal = tipos_animales.get(tipo_animal)
        print(f'Animal elegido: {tipo_animal.__name__}')
        return tipo_animal
        
        
    def asignar_animal(self):
      encargado_encontrado = self.validar_encargado()
      if encargado_encontrado != -1:  
          nombre_animal = pedir_str('Ingrese el nombre del animal: ')
          for animal in self.listanimales:
            if animal.nombre == nombre_animal:
              encargado_encontrado.lista_animales_a_cuidar.append(animal)
              print('Animal asignado')
            else:
              print('Animal no encontrado')
    
    def cambiar_encargado(self):
      nombre_animal = pedir_str('Ingrese el nombre del animal: ')
      for animal in self.listanimales:
        if animal.nombre == nombre_animal:
          nuevo_encargado = self.validar_encargado()
          if nuevo_encargado != -1:
            animal.encargado_cuidar = nuevo_encargado
            print('Animal cambiado')
            print(f'Nuevo encargado: {nuevo_encargado.nombre}')
          
        else:
          print('Animal no encontrado')
          
          
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



gestor.crear_encargado()
gestor.crear_animal()
gestor.asignar_animal()
gestor.cambiar_encargado()