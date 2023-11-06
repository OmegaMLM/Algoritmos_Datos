"""menu
1.   Crear Computadora, indicando tipo y guardar en una lista. Verificando marca y SO de una lista
2.   Listar Computadoras (presentandolos), indicando tipo.
3.   Cambiar SO de una Computadora, verificando una lista de SO disponibles
4.   Listar perifericos
  """
from gestor import *
from prettytable import PrettyTable
def menu():
    gestor = GestorComputadora()
    while True:
        try:
            table = PrettyTable()
            table.field_names = ["Opciones", "Descripción"]
            table.add_row(["1", "Crear computadora"])
            table.add_row(["2", "Listar computadoras"])
            table.add_row(["3", "Cambiar SO de una computadora"])
            table.add_row(["4", "Listar perifericos"])
            print(table)
            opciones = pedir_int("Elija una opción: ")
            match opciones:
                case 1:
                    gestor.crearComputadora()
                case 2:
                    gestor.listarComputadoras()
                case 3:
                    gestor.lista_cambiar_so()
                case 4:
                    gestor.listar_perifericos()
                    
                case _:
                    print("Opcion no valida")
                    
        except Exception as error:
            print(f"Error: {error}. Opcion no valida")