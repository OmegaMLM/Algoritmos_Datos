from gestor import *
from prettytable import PrettyTable
def menu():
    gestor = GestorHabitaciones()
    while True:
        try:
            table = PrettyTable()
            table.field_names= (["Opciones", "Descripción"])
            table.add_row(["1", "Crear Habitaciones"])
            table.add_row(["2", "Cambiar Precio Habitacion"])
            table.add_row(["3", "Mostrar Un Numero De Habitaciones"])
            table.add_row(["4", "Salir"])
            print(table)
            opcion = input('Ingrese una opción: ')
            
            match opcion:
                case '1': 
                    gestor.crear_habitacion()
                
                case '2':
                    gestor.cambiar_precio()
                
                case '3':
                    gestor.mostrar_habitaciones()
                
                case '4':
                    print('Saliendo...')
                    break
                case _:
                    print('Opcion incorrecta')
                
                
        except Exception as error:
            print(error, 'Ingrese una opcion valida')