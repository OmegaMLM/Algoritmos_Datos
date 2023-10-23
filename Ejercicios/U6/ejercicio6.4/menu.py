"""1.   Crear auto, indicando tipo de auto y guardar en una lista
2.   Listar autos (presentandolos), indicando tipo de Vehiculo.
3.   Cambiar velocidad de un Vehiculo
4.   Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
  """
from prettytable import PrettyTable
from gestor import GestorAutos, pedir_int
def menu():
  gestor = GestorAutos()
  while True:
    try:
      table = PrettyTable()
      table.field_names = ["Opciones", "Descripción"]
      table.add_row(["1", "Crear auto"])
      table.add_row(["2", "Listar autos"])
      table.add_row(["3", "Cambiar velocidad"])
      table.add_row(["4", "Calcular tiempo de viaje"])
      print(table)
      opcion = pedir_int("Ingrese una opcion: ")
      match opcion:
        case 1:
          gestor.crear_vehiculo()
        case 2:
          gestor.presentar_todos()
        case 3:
          gestor.cambiar_velocidad()
        case 4:
          gestor.tiempo_de_viaje()
        case _:
          print("Opcion no valida")
    except Exception as error:
      print(f"Error: {error}. Opcion no valida")