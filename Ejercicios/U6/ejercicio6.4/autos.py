'''
###**Ejercicio 6.4**
Crear una clase padre Vehiculos:
*   Constructor debe incluir los atributos (patente,marca,año,origen)
*   Crear metodos para esta clase de:
    1.  Presentarse (patente,marca,año,origen)
    2.  Indicar tipos de vehiculo(Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. Acelerar, Retroceder, obtener_velocidad, setear_velocidad

Crear 3 clases que hereden de la clase padre Vehiculos, con un atributo en particular para cada una
1.   Particular
2.   PickUp
3.   Deportivo
'''

class Vehiculos:
    def __init__(self, patente, marca, anio, origen):
        self.patente = patente
        self.marca = marca
        self.anio = anio
        self.origen = origen
        
    def mostrar_info(self):
      print(f'Patente: {self.patente}, Marca: {self.marca}, Año: {self.anio}, Origen: {self.origen}')
    
    def tipos_vehiculos(self):
      print(f'Soy vehiculo de tipo: {type(self).__name__}')
    
    def acelerar(self):
      pass
    
    def retroceder(self):
      pass
    
    def obtener_velocidad(self):
      pass
    
    def setear_velocidad(self, velocidad):
      pass
    
class Particular(Vehiculos):
  def __init__(self, patente, marca, anio, origen, asientos):
    super().__init__(patente, marca, anio, origen)
    self.asientos = asientos
  
  def acelerar(self):
    print('Acelerando auto particular')

  def retroceder(self):
    print('Retrocediendo auto particular')
  
  def obtener_velocidad(self):
      return self.velocidad
    
  def setear_velocidad(self, velocidad):
      self.velocidad = velocidad
      
class PickUp(Vehiculos):
  def __init__(self, patente, marca, anio, origen, carga):
    super().__init__(patente, marca, anio, origen)
    self.carga = carga  
  def acelerar(self):
    print('Acelerando auto pickup')
  
  def retroceder(self):
    print('Retrocediendo auto pickup')
    
  def obtener_velocidad(self):
      return self.velocidad
    
  def setear_velocidad(self, velocidad):
      self.velocidad = velocidad
      
class Deportivo(Vehiculos):
  def __init__(self, patente, marca, anio, origen, torque):
    super().__init__(patente, marca, anio, origen)
    self.torque = torque
  def acelerar(self):
    print('Acelerando auto deportivo')
  
  def retroceder(self):
    print('Retrocediendo auto deportivo')
    
  def obtener_velocidad(self):
      return self.velocidad
  
  def setear_velocidad(self, velocidad):
      self.velocidad = velocidad
    
  