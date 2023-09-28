from prettytable import PrettyTable
from utility import *
def menu():
  while True:
    try:
      table = PrettyTable()
      table.field_names = ["Opción", "Descripción"]
      table.add_row(["1", "Ver informacion de taxis"])
      table.add_row(["2", "Ver posibles autos y choferes por recorrido"])
      table.add_row(["3", "Modificar chofer segun nombre del auto"])
      table.add_row(["4", "Modificar recorrido segun nombre del auto"])
      table.add_row(["5", "Agregar nuevo taxi"])
      table.add_row(["6", "Observar informacion de chofer"])
      table.add_row(["7", "Salir"])
      table.add_row(["", ""])
      
      print(table)
      
      opcion = int(input('Ingrese una opcion: '))
      match opcion:
        case 1:
          mostrar_taxis()
        case 2:
          recorrido_auto()
        case 3:
          mod_nombre_auto()
        case 4:
          mod_recorrido_auto()
        case 5:
          add_auto()
        case 6:
          info_chofer()
        case 7:
          print('Saliendo...')
          break
        case _:
          print('Introduzca una opcion correcta.')
    except Exception as error:
        print(f"Error: {error}. Introduzca una opcion valida.")