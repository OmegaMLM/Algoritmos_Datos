from prettytable import PrettyTable

'''
Requerimientos:
El programa debe:
*   Contar con un menu donde permita al usuario elegir entre las siguientes funciones:
    1. Permitir al usuario del programa agregar un nuevo videojuego (Indicando: Nombre - Año - Categoria)
      Verificando: Que el nombre no exista previamente, el año este entre 1990 y 2021 y que la categoria corresponda
      con una lista de categorias.(Ayuda: metodo in de list)
      IMPORTANTE: se debe crear una matriz para contener los datos, listas dentro de listas.
    2. Ver lista de videojuegos (Formato: Nombre - Año - Categoria)
    3. Editar la categoria de un video juego verificando que exista la categoria, se edita mediante el nombre.
    4. Agregar categorias al sistema, poniendo automaticamente la primera letra mayuscula (verificando que no exista previamente).
    5. Eliminar una categoria del sistema, verificando previamente su existencia
    6. Salir
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio (minimo un archivo main y otro de funciones)
'''

categorias = ["Accion", "Deportivo", "Estrategia", "Simulacion"]

#Nombre - Año - Categoria
video_juegos=[[],[],[]]

def pedir_int(texto):
  while True:
    try:
      numero = int(input(f"{texto}: "))
      return numero
    except Exception as error:
      print(f"Error: {error}. Introduzca un numero valido")
      
def pedir_str(texto):
  while True:
      string = input(f"{texto}: ")
      return string
    
def pedir_float(texto):
  while True:
    try:
      numero = float(input(f"{texto}: "))
      return numero
    except Exception as error:
      print(f"Error: {error}. Introduzca un numero valido")
      
def add_game():
  while True:
    nombre = pedir_str("Introduzca el nombre del videojuego").lower().capitalize()
    if nombre in video_juegos[0]:
      print("El nombre de ese videojuego ya existe")
    else:
      video_juegos[0].append(nombre)
      print("Nombre agregado")
      break
  while True:
    anio = pedir_int("Introduzca el año del videojuego (Entre 1990 y 2021)")
    if anio >= 1990 and anio <= 2021:
      video_juegos[1].append(anio)
      print("Año agregado")
      break
    else:
      print("Año no válido")
  while True:
    categoria = pedir_str(f"Introduzca la categoria del videojuego (Categorias: {categorias})").lower().capitalize()
    if categoria in categorias:
      video_juegos[2].append(categoria)
      print("Categoría agregada")
      break
    else:
      print("Categoría no válida")
      
def list_games():
  table = PrettyTable()
  table.add_column('Nombre', video_juegos[0])
  table.add_column('Año', video_juegos[1])
  table.add_column('Categoría', video_juegos[2])
  print(table)  

def change_categoria():
    try:
      nombre = pedir_str("Introduzca el nombre del videojuego").lower().capitalize()
      indice = video_juegos[0].index(nombre)
      print(f"Videojuego encontrado: {video_juegos[0][indice]}, categoría actual: {video_juegos[2][indice]}")
      
      while True:
        newnombre = pedir_str(f"Introduzca la nueva categoría (Categorías: {categorias})").lower().capitalize()
        if newnombre in categorias:
          video_juegos[2][indice] = newnombre
          print("Categoría cambiada")
          return
        else:
          print("Categoría no válida")
    except Exception as error:
      print(f"Error: {error}. Videojuego no encontrado")

def add_categoria():
  while True:
    nombre = pedir_str("Introduzca el nombre de la nueva categoría").lower().capitalize()
    if nombre in categorias:
      print("La categoría ya existe")
    else:
      categorias.append(nombre)
      print("Categoría agregada")
      break

def delete_categoria():
  while True:
    nombre = pedir_str("Introduzca el nombre de la categoría a eliminar").lower().capitalize()
    if nombre in categorias:
      categorias.remove(nombre)
      print("Categoría eliminada")
      break
    else:
      print("Categoría no encontrada")
  



