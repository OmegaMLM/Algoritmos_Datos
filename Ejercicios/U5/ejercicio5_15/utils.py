from prettytable import PrettyTable

base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["Prision break", "La casa de papel" , "Los simpsons"]
        }

def mostrar_base():
  table_peliculas = PrettyTable()
  table_series = PrettyTable()
  table_peliculas.add_column("Peliculas", base.get("peliculas")) 
  table_series.add_column("Series", base.get("series")) 
  print(table_peliculas)
  print(table_series)
def add_base():
  while True:
    eleccion = input("¿Que desea agregar? (Peliculas/Series): ").lower()
    match eleccion:
      case "peliculas":
        agregar = input("¿Que pelicula desea agregar? ").lower().capitalize()
        if agregar in base.get("peliculas"):
          print("Pelicula ya existe")
          break
        else:
          base.get("peliculas").append(agregar)
          print("La pelicula agregada")
          break
      case "series":
        agregar = input("¿Que serie desea agregar? ").lower().capitalize()
        if agregar in base.get("series"):
          print("La serie ya existe")
          break
        else:
          base.get("series").append(agregar)
          print("Serie agregada")
          break
      case _: 
        print("Opcion invalida")

def delete_base():
  while True:
    eleccion = input("¿Que desea eliminar? (Peliculas/Series): ").lower()
    match eleccion:
      case "peliculas":
        eliminar = input("¿Que pelicula desea eliminar? ").lower().capitalize()
        if eliminar in base.get("peliculas"):
          base.get("peliculas").remove(eliminar)
          print("Pelicula eliminada")
          break
        else:
          print("La pelicula no existe")
          break
          
      case "series":
        eliminar = input("¿Que serie desea eliminar? ").lower().capitalize()
        if eliminar in base.get("series"):
          base.get("series").remove(eliminar)
          print("Serie eliminada")
          break
        else:
          print("La serie no existe")
          break
          
      case _:
        print("Opcion invalida")
      
def mostrar_rango():
  while True:
    try:
      eleccion = input("¿Que desea mostrar? (Peliculas/Series): ").lower()
      rango1, rango2 = int(input("Introduzca el primer rango: ")), int(input("Introduzca el segundo rango: "))
      match eleccion:
        case "peliculas":
          print(base.get("peliculas")[rango1-1:rango2])
          break
        case "series":
          print(base.get("series")[rango1-1:rango2])
          break
        case _:
          print("Opcion invalida")
    except Exception as error:
      print(error)
      
def mostrar_palabra():
  while True:
    eleccion = input("¿Que desea mostrar? (Peliculas/Series): ").lower()
    match eleccion:
      case "peliculas":
        peliculas_encontradas = []
        palabra = input("Introduzca la palabra a buscar: ")
        for i in base.get("peliculas"):
          split = i.split()
          for j in split:
            if palabra in j:
              peliculas_encontradas.append(i) 
        if len(peliculas_encontradas) == 0:
          print("No se encontraron peliculas")
        else:
          print(f"Se econtraron las siguientes peliculas: {peliculas_encontradas}, con la palabra {palabra}")
        break
      case "series":
        series_encontradas = []
        palabra = input("Introduzca la palabra a buscar: ")
        for i in base.get("series"):
          split = i.split()
          for j in split:
            if palabra in j:
              series_encontradas.append(i) 
        if len(series_encontradas) == 0:
          print("No se encontraron series")
        else:
          print(f"Se econtraron las siguientes series: {series_encontradas}, con la palabra {palabra}")
        break
      case _:
        print("Opcion invalida")
        