"""
*   Tener un menu con 4 opciones: (GestorPeliculas)
    1. Crear una pelicula y guardar el objeto en una lista de peliculas.
    2. Verificar si la pelicula deseada existe en la lista de peliculas.
    3. Pedir a la lista de peliculas, todas las de un año.
    4. Presentar una pelicula de la lista
    5. Cambiar el genero de una pelicula
"""

from peliculas import Pelicula
class GestorPeliculas:
    def __init__(self):
        self.lista_peliculas : list[Pelicula] = []
    
    def crear_pelicula(self):
        nombre = input('Ingrese el nombre: ')
        anio = input('Ingrese el año: ')
        genero = input('Ingrese el genero: ')
        nacionalidad = input('Ingrese la nacionalidad: ')
        puntuacion = input('Ingrese la puntuacion: ')
        pelicula = Pelicula(nombre,anio,genero,nacionalidad,puntuacion)
        self.lista_peliculas.append(pelicula)
    
    def verificar_pelicula(self) -> Pelicula:
        nombre = input('Indique el nombre de la pelicula a verificar: ')
        for pelicula in self.lista_peliculas:
            if nombre == pelicula.nombre:
                print(f'La pelicula {nombre} existe en la lista')
                return pelicula
            else:
              print(f'La pelicula {nombre} no existe en la lista')
              return False

    def buscar_anio(self):
      peliculas_anio = []
      anio = input('Indique el anio a buscar: ')
      for pelicula in self.lista_peliculas:
        if anio == pelicula.anio:
          peliculas_anio.append(pelicula.nombre)
      if len(peliculas_anio) > 0:
        print(f'Las peliculas del anio {anio} son: {peliculas_anio}')
      else:
        print(f'No hay peliculas del anio {anio}')
    
    def presentar_prelicula_lista(self):
      encontrado = self.verificar_pelicula()
      if encontrado != False:
        encontrado.presentar_pelicula()
      else:
        print(f'La pelicula no existe en la lista')
        
    def cambiar_genero_lista(self):
      encontrado = self.verificar_pelicula()
      if encontrado != False:
        encontrado.cambiar_genero(input('Indique el nuevo genero: '))
        print(f'La pelicula {encontrado.nombre} fue modificada, con el genero {encontrado.genero}')
      else:
        print(f'La pelicula no existe en la lista')

      