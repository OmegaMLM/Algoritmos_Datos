from prettytable import PrettyTable

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


#Opcion 1      
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

#Opcion 2 - Utilizacion de PrettyTable     
def list_games():
  table = PrettyTable()
  table.add_column('Nombre', video_juegos[0])
  table.add_column('Año', video_juegos[1])
  table.add_column('Categoría', video_juegos[2])
  print(table)  

#Opcion 3
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

#Opcion 4
def add_categoria():
  while True:
    nombre = pedir_str("Introduzca el nombre de la nueva categoría").lower().capitalize()
    if nombre in categorias:
      print("La categoría ya existe")
    else:
      categorias.append(nombre)
      print("Categoría agregada")
      break
    
#Opcion 5
def delete_categoria():
  while True:
    nombre = pedir_str("Introduzca el nombre de la categoría a eliminar").lower().capitalize()
    if nombre in categorias:
      categorias.remove(nombre)
      print("Categoría eliminada")
      break
    else:
      print("Categoría no encontrada")
  



