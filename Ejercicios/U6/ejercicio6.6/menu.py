"""     1. Crear instancias de choferes y guardarlos en una lista de choferes
    2. Crear instancias de Autos (verificando que haya choferes para ese auto) y guardarlos en una lista de autos
    3. Modificar el chofer de un auto
    4. Modificar el lugar de residencia del chofer indicando su nombre
    5. imprmiir lista de choferes (con toda su informacion)
    6. imprimir lista de autos (con toda su informacions)
"""

from gestor import GestorTaxis, pedir_int
from prettytable import PrettyTable

def menu():
  table = PrettyTable()
  table.field_names = ["Opciones", "Descripción"]
  table.add_row(["1", "Crear choferes"])
  table.add_row(["2", "Crear autos"])
  table.add_row(["3", "Modificar chofer"])
  table.add_row(["4", "Cambiar lugar de residencia"])
  table.add_row(["5", "Listar choferes"])
  table.add_row(["6", "Listar autos"])
  table.add_row(["7", "Salir"])
  print(table)
  while True:
    try:
      eleccion = pedir_int("Elija una opción: ")
      match eleccion:
        case 1:
          GestorTaxis.crear_chofer()
        case 2:
          GestorTaxis.crear_auto()
        case 3:
          GestorTaxis.modificar_chofer()
        case 4:
          GestorTaxis.modificar_residencia()
        case 5:
          GestorTaxis.listar_choferes()
        case 6:
          GestorTaxis.listar_autos()
        case 7:
          print("Saliendo")
          break
        case _: 
          print("Opcion no valida")
    except Exception as error:
      print(f"Error: {error}. Opcion no valida")
  
