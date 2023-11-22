from gestor import *
from prettytable import PrettyTable
def menu():
    gestor = GestorEvento()
    
    while True:
        try:
            table = PrettyTable()
            table.field_names = ["Opciones", "Descripción"]
            table.add_row(["1", "Crear Evento"])
            table.add_row(["2", "Listar Eventos"])
            table.add_row(["3", "Salir"])
            print(table)
            opcion = pedir_int("Ingrese una opcion: ")
            match opcion:
                case 1:
                    gestor.crear_evento()
                case 2:
                    gestor.leer_archivo()
                case 3:
                    print("Saliendo...")
                    break
                case  _:
                    print("Opcion incorrecta")
        except Exception as e:
            print(f"Error: {e}. Ingrese un dato valido")