"""
*   Tener un menu con 4 opciones: (GestorPeliculas)
    1. Crear una pelicula y guardar el objeto en una lista de peliculas.
    2. Verificar si la pelicula deseada existe en la lista de peliculas.
    3. Pedir a la lista de peliculas, todas las de un año.
    4. Presentar una pelicula de la lista
    5. Cambiar el genero de una pelicula
"""
from prettytable import PrettyTable
from gestor import GestorPeliculas

def menu():
    obj_gestor = GestorPeliculas()
    while True:
        try:
            table = PrettyTable()
            table.field_names = ["Opciones", "Descripción"]
            table.add_row(["1", "Crear Pelicula"])
            table.add_row(["2", "Verificar si la pelicula existe"])
            table.add_row(["3", "Mostrar todas las peliculas de un anio"]) 
            table.add_row(["4", "Presentar una pelicula"])
            table.add_row(["5", "Cambiar un genero de una pelicula"])
            table.add_row(["6", "Salir"])
            print(table)

            eleccion = int(input('Ingrese una opcion: '))
            match eleccion:
                case 1:
                    obj_gestor.crear_pelicula()
                case 2:
                    obj_gestor.verificar_pelicula()
                case 3:
                    obj_gestor.buscar_anio()
                case 4:
                    obj_gestor.presentar_prelicula_lista()
                case 5:
                    obj_gestor.cambiar_genero_lista()
                case 6:
                    print("Saliendo")
                    break
                case _:
                    print("Opcion invalida")
        except Exception as error:
          print(error)
          
if __name__ == '__main__':
    menu()