'''
El programa debe:

-   Contar con una Clase Evento con los atributos (nombre_evento (único), fecha, hora, lugar)
-   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo más: - EventoPersonal (Atributo: organizador (nombre de la grupo que organiza)) - EventoLaboral (Atributo: obligatorio "True o False" (por defecto = True))
-   Se deben crear 4 métodos para la clase padre Evento (que heredaran las clases hijas): 1. Mostrar información: Que indique el nombre_evento, fecha y lugar del evento 2. Obtener tipo de evento (tipo de clases heredadas o padre) 3. Setear Fecha y Hora (Setearán la Fecha y Hora en una misma función) 4. Setear lugar (Setear el lugar)
'''

class Evento:
    def __init__(self, nombre_evento: str, fecha: str, hora: str, lugar: str):
        self.nombre_evento = nombre_evento
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar

    def mostrar_info(self):
        print(f'Nombre del evento: {self.nombre_evento}, Fecha: {self.fecha}, Hora: {self.hora}, Lugar: {self.lugar}')
        
    def obtener_tipo_evento(self):
        return self.__class__.__name__
    
    def setear_hora(self, hora, fecha):
        self.fecha = fecha
        self.hora = hora
    
    def setear_lugar(self, lugar):
        self.lugar = lugar
    

class EventoPersonal(Evento):
    def __init__(self, nombre_evento: str, fecha: str, hora: str, lugar: str, organizador: str):
        super().__init__(nombre_evento, fecha, hora, lugar)
        self.organizador = organizador

    def mostrar_info(self):
        print(f'Nombre del evento: {self.nombre_evento}, Fecha: {self.fecha}, Hora: {self.hora}, Lugar: {self.lugar}, Organizador: {self.organizador}')
        
class EventoLaboral(Evento):
    def __init__(self, nombre_evento: str, fecha: str, hora: str, lugar: str, obligatorio: bool = True):
        super().__init__(nombre_evento, fecha, hora, lugar)
        self.obligatorio = obligatorio

    def mostrar_info(self):
        print(f'Nombre del evento: {self.nombre_evento}, Fecha: {self.fecha}, Hora: {self.hora}, Lugar: {self.lugar}, Obligatorio: {self.obligatorio}')