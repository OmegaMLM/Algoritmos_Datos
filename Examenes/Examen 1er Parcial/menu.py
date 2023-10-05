from utils import *
from prettytable import PrettyTable

def menu():
    while True:
        table = PrettyTable()
        table.field_names= (["Opciones", "Descripción"])
        table.add_row(["1", "Ver informacion de alumnos"])
        table.add_row(["2", "Agregar un alumno"])
        table.add_row(["3", "Cambiar la edad"])
        table.add_row(["4", "Ver materias"])
        table.add_row(["5", "Agregar materias"])
        table.add_row(["6", "Salir"])
        print(table)
        opcion = input('Ingrese una opción: ')
        if(opcion == "1"):
            print_lista()
        elif(opcion == "2"):
            add_alumno()
        elif(opcion == "3"):
          edit_edad()
        elif(opcion == "4"):
            print_materias()
        elif(opcion == "5"):
            add_materias()
        elif(opcion == "6"):
            print("Saliendo...")
            break
        else:
            print('Opcion incorrecta')