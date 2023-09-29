from utilidad import *

def menu():
    while True:
        menu = """--Programa de Agenda--
    1. Agregar un nuevo videojuego
    2. Ver lista de videojuegos (Formato: Nombre - Año - Categoria)
    3. Editar la categoria de un video juego verificando que exista la categoria, se edita mediante el nombre.
    4. Agregar categorias al sistema, poniendo automaticamente la primera letra mayuscula (verificando que no exista previamente).
    5. Eliminar una categoria del sistema, verificando previamente su existencia
    6. Salir
Ingrese una opcion: """
        opcion = input(menu)
        if(opcion == "1"):
          add_game()
        elif(opcion == "2"):
          list_games()
        elif(opcion == "3"):
          change_categoria()
        elif(opcion == "4"):
          add_categoria()
        elif(opcion == "5"):
          delete_categoria()
        elif(opcion == "6"):
            print("Saliendo...")
            break
        else:
            print('Opcion incorrecta')

if __name__ == "__main__":
    main()