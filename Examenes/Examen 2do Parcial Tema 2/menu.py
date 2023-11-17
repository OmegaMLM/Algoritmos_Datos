from gestor import *
from prettytable import PrettyTable


def menu():
    gestor = GestorBiblioteca()
    
    while True:
        try:
            table = PrettyTable()
            table.field_names = ["Opciones", "Descripción"]
            table.add_row(["1", "Agregar Libro"])
            table.add_row(["2", "Listar Libros"])
            table.add_row(["3", "Alquilar/Devolver Libro"])
            table.add_row(["4", "Salir"])
            print(table)
            opcion = pedir_str("Ingrese una opcion: ")
            match opcion:
                case '1':
                    gestor.crear_libro()
                case '2':
                    gestor.listar_libros()
                case '3':
                    gestor.alquilar()
                case '4':
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion incorrecta")
        except Exception as e:
            print(f"Error: {e}. Ingrese un dato valido")