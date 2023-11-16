'''Requerimientos:
El programa debe:
*   Contar con una Clase Habitacion con los atributos (numero (único), max_pesonas (int), precio (float))
*   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo más:
        - HabitacionClasica (Atributo: cant_televisores (int))
        - HabitacionPremium (Atributo: Jacuzzi "True o False" (por defecto = True))
        
*   Se deben crear los siguientes métodos para la clase padre Habitacion (que heredaran las clases hijas):
        1. Mostrar información: Que indique el numero, max_personas y precio
            -  Este metodo debe ser creado en la clase padre y las hijas, ya que las clases hijas deben mostrar tambien sus atributos
        2. Setear y obtener max_personas
        3. Setear y obtener precio
        4. Obtener tipo de clase
'''

class Habitacion:
    def __init__(self, numero : int , max_personas: int, precio: float):
        self.numero = numero
        self.max_personas = max_personas
        self.precio = precio
        
    def mostrar_informacion(self):
        print(f'Numero: {self.numero}, Max personas: {self.max_personas}, Precio: {self.precio}')
        
    def set_max_personas(self, max_personas):
        self.max_personas = max_personas
        return self.max_personas
    
    def set_precio(self, precio):
        self.precio = precio
        return self.precio
    
    def get_tipo_clase(self):
        return self.__name__
    
class HabitacionComun(Habitacion):
    def __init__(self, numero : int , max_personas: int,precio: float):
        super().__init__(numero,max_personas,precio)


class HabitacionClasica(Habitacion):
    def __init__(self, numero : int , max_personas: int, precio: float, cant_televisores: int):
        super().__init__(numero,max_personas, precio)
        self.cant_televisores = cant_televisores
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Cant televisores: {self.cant_televisores}')
        
    def set_cant_televisores(self, cant_televisores):
        self.cant_televisores = cant_televisores
        return self.cant_televisores
    
class HabitacionPremium(Habitacion):
    def __init__(self, numero : int , max_personas: int,precio: float, jacuzzi: bool):
        super().__init__(numero,max_personas,precio)
        self.jacuzzi = jacuzzi
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Jacuzzi: {self.jacuzzi}')
        
    def set_jacuzzi(self, jacuzzi):
        self.jacuzzi = jacuzzi
        return self.jacuzzi
    