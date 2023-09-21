from utility import add_stock, consult_stock, delete_stock
from prettytable import PrettyTable
def menu():
  while True:
    try:
      menu_table = PrettyTable()
      menu_table.field_names = ["Opciones", "Descripcion"]
      menu_table.add_row(["1", "Agregar stock"])
      menu_table.add_row(["2", "Consultar stock"])
      menu_table.add_row(["3", "Eliminar stock"])
      menu_table.add_row(["4", "Salir"])
      print(menu_table)
      
      opcion = int(input('Ingrese una opcion: '))
      match opcion:
        case 1:
          add_stock()
        case 2:
          consult_stock()
        case 3:
          delete_stock()
        case 4:
          print('Saliendo...')
          break
        case _:
          print('Introduzca una opcion correcta.')
    except Exception as error:
        print(f"Error: {error}. Introduzca una opcion valida.")