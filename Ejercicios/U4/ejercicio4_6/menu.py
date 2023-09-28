from utils import *

def menu():
  while True:
    try:
      table = PrettyTable()
      table.field_names = ["Opciones", "Descripción"]
      table.add_row(["1", "Ver informacion de productos"])
      table.add_row(["2", "Comprar un producto"])
      table.add_row(["3", "Add stock"])
      table.add_row(["4", "Cambiar Precio"])
      table.add_row(["5", "Salir"])
      print(table)
      
      
      opcion = int(input('Ingrese una opcion: '))
      
      match opcion:
        case 1:
          product_menu()
        case 2:
          producto, stock = product()
          metodo = metod()
          pay(metodo, producto, stock)
        case 3:
          add_stock()
        case 4:
          change_price()
        case 5:
          print('Saliendo...')
          break
        case _:
          print('Ingrese una opcion valida.')
        
    except Exception as e:
      print(f'Error: {e}. Ingrese una opcion valida.')