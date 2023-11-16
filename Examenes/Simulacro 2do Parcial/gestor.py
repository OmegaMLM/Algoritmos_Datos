'''*   Se debe crear una clase GestorHabitaciones que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de una habitacion y guárdalos en una lista de habitaciones. 
        1.1) Se debe verificar que tipo de instancia de Habitacion a crear y los parámetros. IMPORTANTE!: clase hijas verificar y pedir parámetros
             - numero: debe ser único
             - max_personas: verificar que sea un numero entero y este entre 2 y 6 inclusives.
             - precio: se debe pedir en pesos pero se debe guardar en dolares (1 dolar -> 900 pesos)
        1.2) Clases hijas:
             - cant_televisores: verificar que sea entero entre 0 y 3 incluses
             - Jacuzzi: verificar que sea True o False (boolean)
             
        1.3) Al crear una Habitacion es necesario logearlo (Escribir en una línea nueva: numero,max_personas,precio,tipo_de_clase)) 
             en un archivo llamado historial_habitaciones.txt (Crear función en el mismo gestor). IMPORTANTE!: verificar permisos y extension
    2.   Cambiar precio de habitacion, seleccionando su numero: Se debe cambiar el precio de la habitacion dependiendo de la cant max de 
         personas que contenga y el tipo de habitacion:
         - Se debe leer el diccionario por el tipo de habitacion y multiplicar ese precio por la cantidad de personas.
         Ej. Precio hab clasica = 400 (CL)* max_personas = 400 * 5 = 2000 IMPORANTE! solo se le pide el numero de habitacion al usuario
    3.   Pedir al usuario un numero y listar esa cantidad de habitaciones de la lista, verificando que hayan esa cantidad de habitaciones'''
    
from clase_habitaciones import *
    

class GestorHabitaciones:
    def __init__(self):
        self.lista_habitaciones : list[Habitacion] = []
        self.precio_hab = precio_habitaciones = {
    "HabitacionComun": 300, 
    "HabitacionClasica": 400,
    "HabitacionPremium": 500
    }
        self.numeros_habitaciones = set([])
        
        
    #Opcion 1
    def crear_habitacion(self):
        tipo_habitacion = self.validar_tipo()
        numero = self.verificar_numero()
        max_personas = validar_rango('Ingrese la cantidad maxima de personas: ', 2, 6)
        precio = self.definir_precio(tipo_habitacion)
        
        if tipo_habitacion == HabitacionClasica:
            cant_televisores = validar_rango('Ingrese la cantidad de televisores: ', 0, 3)
            habitacion = tipo_habitacion(numero, max_personas, precio, cant_televisores)
            self.lista_habitaciones.append(habitacion)
        elif tipo_habitacion == HabitacionPremium:
            jacuzzi = self.validar_bool('¿Tiene jacuzzi?')
            habitacion = tipo_habitacion(numero, max_personas,precio, jacuzzi)
            self.lista_habitaciones.append(habitacion)
        else:
            habitacion = tipo_habitacion(numero, max_personas,precio)
            self.lista_habitaciones.append(habitacion)
        self.escribir_archivo()
        
    def verificar_numero(self):
        while True:
            numero_ingresado = validar_int('Ingrese el numero de la habitacion: ')
            if numero_ingresado in self.numeros_habitaciones:
                print('La habitacion ya existe')
            else:
                self.numeros_habitaciones.add(numero_ingresado)
                return numero_ingresado
            
    def validar_bool(self, text):
        opcion = input(f'{text}, (Si o No): ').lower()
        while True:
            if opcion == 'si':
                return True
            elif opcion == 'no':
                return False
            else:
                print('Opcion incorrecta')
    
    def validar_tipo(self):
        tipos_hab = {
            'HabitacionComun': HabitacionComun,
            'HabitacionClasica': HabitacionClasica,
            'HabitacionPremium': HabitacionPremium
        }
        
        
        while True:
            for tipos in tipos_hab.keys():
                print(tipos, end = ' - ')
            print()
            tipo = input('Ingrese el tipo de habitacion: ')
            if tipo in tipos_hab:
                return tipos_hab[tipo]
            else:
                print(f'El tipo de habitacion {tipo} no existe') 
                
        
    def escribir_archivo(self):
        with open('historial_habitaciones.txt', 'a') as archivo:
            for habitacion in self.lista_habitaciones:
                archivo.write(f'Numero de Habitacion:{habitacion.numero}, Max personas: {habitacion.max_personas}, Precio: {habitacion.precio}, Tipo de Habitacion: {habitacion.__class__.__name__}\n')
    def definir_precio(self, tipo_habitacion):
        for tipo in self.precio_hab.keys():
            if tipo == tipo_habitacion.__name__ :
                return self.precio_hab[tipo]
            
            
    #Opcion 2
    def cambiar_precio(self):
        while True:
            numero_buscar = validar_int('Ingrese el numero de habitacion: ')
            for habitacion in self.lista_habitaciones:
                if habitacion.numero == numero_buscar:
                    nuevo_precio = habitacion.max_personas * self.definir_precio(habitacion.__class__)
                    habitacion.set_precio(nuevo_precio)
                    print(f'El precio de la habitacion {habitacion.numero} ha sido cambiado a ${nuevo_precio}')
                    return
                else:
                    print(f'La habitacion {habitacion.numero} no existe')
                    
                    
    #Opcion 3
    def mostrar_habitaciones(self):
        cant_habitaciones = len(self.lista_habitaciones)
        habitaciones_a_mostrar = validar_int('Ingrese la cantidad de habitaciones a mostrar: ')
        if habitaciones_a_mostrar <= cant_habitaciones:
            for i in range(cant_habitaciones):
                    self.lista_habitaciones[i].mostrar_informacion()
        else:
            print('No hay habitaciones suficientes para mostrar')
        
def validar_int(text):
    while True:
        try:
            numero = int(input(text))
            return numero
        except Exception as e:
            print(f'Error: {e}. Ingrese un dato valido')

def validar_rango(text, min, max):
    while True:
        try:
            numero = int(input(text))
            if numero >= min and numero <= max:
                return numero
            else:
                print(f'Error. El numero debe estar entre {min} y {max}')
        except Exception as e:
            print(f'Error: {e}. Ingrese un dato valido')
            
            