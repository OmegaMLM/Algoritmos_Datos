'''
Crear una clase de Pelicula:
*   Cuyo constructutor debe inicializar los atributos nombre, año, genero, nacionalidad, puntuacion
*   Se deben crear 4 metodos en la clase:
    1.  Presentar la pelicula: La pelicula {nombre} de {genero} del {año} obtuvo una puntuacion de {puntuacion}  y fue filmada en {nacionalidad}
    2.  Retornar si el año de la pelicula es mayor o igual o menor al pasado por parametro
    3. Cambiar el genero de una pelicula
    4. Modificar puntuacion de la pelicula (entre 1 y 10)'''

class Pelicula:
    def __init__(self, nombre, anio, genero, nacionalidad, puntuacion):
        self.nombre = nombre
        self.anio = anio
        self.genero = genero
        self.nacionalidad = nacionalidad
        self.puntuacion = puntuacion

    def presentar_pelicula(self):
        print(f"""La pelicula es {self.nombre}, de genero {self.genero},
del año {self.anio}, obtuvo la puntuacion de {self.puntuacion}, y fue
filmada nacionalidad {self.nacionalidad}""")

    def retornar_anio(self, anio):
        if self.anio < anio:
            return "Es menor al pasado por parametro"
        elif self.anio == anio:
            return "Es igual al pasado por parametro"
        elif self.anio > anio:
            return "Es mayor al pasado por parametro"
        else:
            return "Algo fallo"

    def cambiar_genero(self,nuevo_genero):
        self.genero = nuevo_genero

    def modifico_puntuacion(self,nueva_puntuacion):
        self.puntuacion = nueva_puntuacion