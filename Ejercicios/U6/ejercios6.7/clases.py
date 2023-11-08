"""-   Simular un programa de gestion de animales de un zoologico, que cuente con dos clases Animales y Empleados
-   La Clase Animales tiene los atributos (nombre, tipo_animal, fecha_nacimiento, encargado_cuidar (Nombre de objeto empleado))
    -   Crear 3 clases que hereden de animal segun su sector del zoologico)
        1. Animales en jaulas.
        2. Animales sueltos.
        3. Animales en el agua
-   La Clase Empleados tiene los atributos (legajo, nombre, apellido, lista_animales_a_cuidar(clase animal))
    -   un empleado puede cuidar animales de diferentes sectores
"""

class Encargado:
    def __init__(self, legajo: int, nombre: str, apellido: str):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.lista_animales_a_cuidar = lista_animales_a_cuidar
        
class Animales:
    def __init__(self, nombre: str, tipo_animal: Animales, fecha_nacimiento:int, encargado_cuidar: Encargado = None):
        self.nombre = nombre
        self.tipo_animal = tipo_animal
        self.fecha_nacimiento = fecha_nacimiento
        self.encargado_cuidar = encargado_cuidar
        
        
class AnimalesJaula(Animales):
    def __init__(self, nombre: str, tipo_animal: str, fecha_nacimiento:int, encargado_cuidar: Encargado = None):
        super().__init__(nombre, tipo_animal, fecha_nacimiento, encargado_cuidar)
        
class AnimalesSueltos(Animales):
    def __init__(self, nombre: str, tipo_animal: str, fecha_nacimiento:int, encargado_cuidar: Encargado = None):
        super().__init__(nombre, tipo_animal, fecha_nacimiento, encargado_cuidar)
        
class AnimalesAgua(Animales):
    def __init__(self, nombre: str, tipo_animal: str, fecha_nacimiento:int, encargado_cuidar: Encargado = None):
        super().__init__(nombre, tipo_animal, fecha_nacimiento, encargado_cuidar)
        
        
