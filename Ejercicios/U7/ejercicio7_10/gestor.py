import os
import json

'''
### **Ejercicio 7.10**

Crea una clase llamada Empleado con los siguientes atributos:

-   nombre
-   edad
-   puesto

Cada vez que se cree un objeto tiene que ser guardado los datos en un json con el formato

"empleados": [
{"nombre": empleado1.nombre, "edad": empleado1.edad, "puesto": empleado1.puesto},
]

Crear una funcion de la clase que lea la informacion del archivo e imprima en formato de tabla (Un bucle for)

'''

class Empleado:
    def __init__(self, nombre, edad, puesto):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        
        dict = { 'nombre': self.nombre, 'edad': self.edad, 'puesto': self.puesto }
        
        
    def crear_empleado(self):
        nombre = input('Introduce el nombre del empleado: ')
        edad = input('Introduce la edad del empleado: ')
        puesto = input('Introduce el puesto del empleado: ')
        return Empleado(nombre, edad, puesto)
    
    def guardar_en_json(self, empleado):
        datos_empleados = {'empleados': [
            {
            'nombre': empleado.nombre, 
            'edad': empleado.edad, 
            'puesto': empleado.puesto}
        ]
                        }
        
        nombre_archivo = input('Introduce el nombre del archivo: ')
        fichero = open(f'{nombre_archivo}.json', 'a+')
        json.dump(datos_estudiantes, fichero)
        fichero.close()

gestor = Empleado()
empleado = gestor.crear_empleado()

print(empleado.nombre)