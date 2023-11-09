

from gestor import GestorZoologico, pedir_int
from prettytable import PrettyTable


gestor = GestorZoologico()
def menu():
  table = PrettyTable()
  table.field_names = ["Opciones", "Descripción"]
  table.add_row(["1", "Crear Encargado "])
  table.add_row(["2", "Crear Animales"])
  table.add_row(["3", "Asignar Animal"])
  table.add_row(["4", "Cambiar encargado"])
  table.add_row(["5", "Imprimir lista animales"])
  table.add_row(["6", "Imprimir ista Encargados"])
  table.add_row(["7", "Salir"])
  print(table)
  while True:
    try:
      eleccion = pedir_int("Elija una opción: ")
      match eleccion:
        case 1:
          gestor.crear_encargado()
        case 2:
          gestor.crear_animal()
        case 3:
          gestor.asignar_animal()
        case 4:
          gestor.cambiar_encargado()
        case 5:
          gestor.presentar_animales()
        case 6:
          gestor.presentar_empleados()
        case 7:
          print("Saliendo")
          break
        case _: 
          print("Opcion no valida")
    except Exception as error:
      print(f"Error: {error}. Opcion no valida")
  
