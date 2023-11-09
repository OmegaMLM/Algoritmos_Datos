from clase import LectorDeArchivos
from prettytable import PrettyTable

def menu():
  lector = LectorDeArchivos()
  lector.abrir_archivo("archivo.txt")
  
  table = PrettyTable()
  table.field_names = ["Opciones", "Descripción"]
  table.add_row(["1", "Leer archivo"])
  table.add_row(["2", "Contar comas"])
  table.add_row(["3", "Contar cantidad de letras de 3 caracteres"])
  table.add_row(["4", "Quitar una palabra"])
  table.add_row(["5", "Salir"])
  print(table)
  while True:
    try:
      eleccion = pedir_int("Elija una opción: ")
      match eleccion:
        case 1:
          lector.leer_archivo()
        case 2:
          lector.encontrar_comas()
        case 3:
          lector.palabras_3_caracteres()
        case 4:
          lector.sacar_palabra()
        case 5:
          print("Saliendo...")
          lector.cerrar_archivo()
          break
        case _: 
          print("Opcion no valida")
    except Exception as error:
      print(f"Error: {error}. Opcion no valida")
  
