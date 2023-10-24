"""Crear una clase padre Computadoras:
*   Constructor debe incluir los atributos (id_modelo,listaPerifericos,SO)
*   Crear metodos para esta clase de:
    1.  Presentarse (id_modelo,listaPerifericos,SO)
    2.  Indicar tipo de Computadora (Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. agregar_perifericos,CambiarSO

Crear 2 clases que hereden de la clase padre Computadoras, con un atributo en particular para cada una
1.   Escritorio
2.   Notebook
  """

class Computadoras:
    def __init__(self,id_modelo,listaPerifericos,SO,marca):
        self.id_modelo = id_modelo
        self.listaPerifericos = listaPerifericos
        self.SO = SO
        self.marca = marca
        
    def presentarse(self):
        print(f'Modelo: {self.id_modelo}, SO: {self.SO}, Perifericos: {self.listaPerifericos}, Marca: {self.marca}')
    
    def tipo_computadora(self):
        print(f'El tipo de computadora es {type(self).__name__}')
    
    def agregar_perifericos(self, perifericos):
        pass
    
    def cambiar_so(self, nuevo_so):
        pass
      
class Escritorio(Computadoras):
    def __init__(self, id_modelo, listaPerifericos, SO, marca, grafica):
        super().__init__(id_modelo, listaPerifericos, SO, marca)
        self.grafica = grafica
        
    def agregar_perifericos(self, perifericos):
        self.listaPerifericos.append(perifericos)
        
    def cambiar_so(self, nuevo_so):
        self.SO = nuevo_so
        
class Notebook(Computadoras):
    def __init__(self, id_modelo, listaPerifericos, SO, marca, bateria):
        super().__init__(id_modelo, listaPerifericos, SO, marca)
        self.bateria = bateria
        
    def agregar_perifericos(self, perifericos):
        self.listaPerifericos.append(perifericos)
        
    def cambiar_so(self, nuevo_so):
        self.SO = nuevo_so