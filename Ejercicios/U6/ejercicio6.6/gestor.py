'''
1. Crear instancias de choferes y guardarlos en una lista de choferes
    2. Crear instancias de Autos (verificando que haya choferes para ese auto) y guardarlos en una lista de autos
    3. Modificar el chofer de un auto
    4. Modificar el lugar de residencia del chofer indicando su nombre
    5. imprmiir lista de choferes (con toda su informacion)
    6. imprimir lista de autos (con toda su informacions)

-   Se deben crear los metodos correspondientes para las funciones del menu en las clases correspondientes
-   Gestionar posibles errores
-   Estructurar el programa a criterio propio
'''


from clases import *

class GestorTaxis:
  def __init__(self):
    self.listAutos : list[Auto] = []
    self.listChoferes : list[Chofer] = []
    
  def crear_chofer(self):
    for i in range(pedir_int("Ingresa la cantidad de choferes a crear: ")) :
      print("")
      nombre = pedir_str("Ingresa el nombre del chofer: ")
      apellido = pedir_str("Ingresa el apellido del chofer: ")
      dni = pedir_int("Ingresa el dni del chofer: ")
      fecha_nacimiento = pedir_str("Ingresa la fecha de nacimiento del chofer (dd/mm/aaaa): ")
      residencia = pedir_str("Ingresa la residencia del chofer: ")
      chofer = Chofer(nombre, apellido, dni, fecha_nacimiento, residencia)
      self.listChoferes.append(chofer)
    
  def crear_auto(self):
    for i in range(pedir_int("Ingresa la cantidad de autos a crear: ")) :
      print("")
      patente = pedir_str("Ingresa la patente del auto: ").upper()
      modelo = pedir_str("Ingresa el modelo del auto: ")
      anio = pedir_int("Ingresa el anio del auto: ")
      marca = pedir_str("Ingresa la marca del auto: ")
      
      nombre_chofer = self.verificar_nombre()
      auto = Auto(patente, modelo, anio, marca, nombre_chofer)
      self.listAutos.append(auto)

  def verificar_nombre(self):
    nombres_disponibles = []
    for chofer in self.listChoferes:
        nombres_disponibles.append(chofer.nombre)
    while True:
      print(f'Los choferes disponibles son: {nombres_disponibles}')
      nombre = pedir_str('Elija el nombre del chofer: ')
      for chofer in self.listChoferes:
        if nombre == chofer.nombre:
          print(f'Asignado al chofer {nombre}')
          return chofer
      print(f'El chofer {nombre} no existe en la lista')
      
  def modificar_chofer(self):
    nombres_disponibles = []
    for chofer in self.listChoferes:
        nombres_disponibles.append(chofer.nombre)
    while True:
      patente = pedir_str('Elija la patente del auto a modificar: ')
      for auto in self.listAutos:
        print(auto.patente)
        if patente == auto.patente:
          while True:
            print(f'Choferes disponibles: {nombres_disponibles}')
            nombre = pedir_str('Elija el nombre del chofer: ')
            for chofer in self.listChoferes:
              if nombre == chofer.nombre:
                auto.nombre_Chofer = chofer
                print(f'El chofer {nombre} fue modificado')
                return
            print(f'El chofer {nombre} no existe en la lista')

      print(f'El auto con la patente {patente} no existe en la lista')
          
  def modificar_residencia(self):
      dni = pedir_int('Elija el dni del chofer: ')
      for chofer in self.listChoferes:
        if dni == chofer.dni:
          chofer.residencia = pedir_str('Elija la nueva residencia: ')
          print(f'La residencia del chofer {chofer.nombre} fue modificada')
          return
      print(f'El chofer con el dni {dni} no existe en la lista')
  def mostrar_choferes(self):
    for chofer in self.listChoferes:
      chofer.presentarse()
      
  def mostrar_autos(self):
    for auto in self.listAutos:
      auto.presentarse()
      
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
        