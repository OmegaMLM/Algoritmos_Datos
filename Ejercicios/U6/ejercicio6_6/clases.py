'''-   Simular una empresa de taxis que cuente con dos clases: Autos y Chofer
-   La Clase auto tiene los atributos (patente, modelo, año, marca, nombre_Chofer (objeto clase Choferes))
-   La Clase Chofer tiene los atributos (nombre, apellido, dni, fecha nacimiento, Residencia)'''

class Chofer:
  def __init__(self, nombre:str, apellido:str, dni:int, fecha_nacimiento:str, residencia:str):
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.fecha_nacimiento = fecha_nacimiento
    self.residencia = residencia
    
  def presentarse(self):
    print(f'Nombre: {self.nombre}')
    print(f'Apellido: {self.apellido}')
    print(f'DNI: {self.dni}')
    print(f'Fecha de nacimiento: {self.fecha_nacimiento}')
    print(f'Residencia: {self.residencia}')
    
class Auto:
  def __init__(self, patente:str, modelo:str, anio:int, marca:str, nombre_Chofer:Chofer):
    self.patente = patente
    self.modelo = modelo
    self.anio = anio
    self.marca = marca
    self.nombre_Chofer = nombre_Chofer
    
  def presentarse(self):
    print(f'Patente: {self.patente}')
    print(f'Modelo: {self.modelo}')
    print(f'Anio: {self.anio}')
    print(f'Marca: {self.marca}')
    print(f'Chofer: {self.nombre_Chofer.nombre}')
    