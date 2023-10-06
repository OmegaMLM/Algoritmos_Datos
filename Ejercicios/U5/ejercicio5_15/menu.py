from prettytable import PrettyTable
from utils import *

def menu():
  while True:
    try:
      table = PrettyTable()
      table.field_names = ["Opción", "Descripción"]
      table.add_row(["1", "Ver peliculas y series"])
      table.add_row(["2", "Agregar series o peliculas"])
      table.add_row(["3", "Eliminar series o peliculas"])
      table.add_row(["4", "Mostrar por rango"])
      table.add_row(["5", "Buscar palabras en los titulos"])
      table.add_row(["6", "Salir"])
      print(table)
      
      eleccion = int(input('Ingrese una opción: '))
      match eleccion:
        case 1:
          mostrar_base()
        case 2:
          add_base()
        case 3:
          delete_base()
        case 4:
          mostrar_rango()
        case 5:
          mostrar_palabra()
        case 6:
          print("Saliendo")
          break
        
    except Exception as error:
        print(f"Error: {error}. Introduzca una opción valida.")