'''
-   Se debe crear una clase GestorEvento que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de un evento y guárdalos en una lista de eventos.
        1.1) Se debe verificar que tipo de instancia de evento a crear y los parámetros. IMPORTANTE!: clase hijas verificar y pedir parámetros - nombre_evento: debe ser único. Ayuda: verificar que ningun objet de la lista tenga ese nombre - Fecha: formato (dd/mm/yyyy) -> verificar unicamente que la longitud del string sea 10. Ayuda!: Metodo len() - Hora: formato (hh:mm) -> no es necesario verificar - Lugar: sin formato especifico -> no es necesario verificar
        1.2) Al crear un evento es necesario logearlo (Escribir en una línea nueva: nombre_evento-Fecha-Hora-Lugar-Tipo_de_evento(tipo de clase))
        en un archivo llamado lista_eventos.txt (Crear función en el mismo gestor). IMPORTANTE!: verificar permisos
        1.3) En caso que la instancia del evento sea EventoPersonal. - Para el organizador, el usuario debe elegir a través de una clave (mostradas por el programa)
        desde un diccionario de organizadores. - En caso que no exista el organizador deseado debe ser "incognito" (AYUDA: Funcion get de diccionarios)
    2.  Listar eventos disponibles, leyendo la lista_evetos.txt. IMPORTANTE!: Leer el archivo, no la lista.

-   Se deben crear los métodos correspondientes para las funciones del menú en las clases correspondientes
-   Gestionar posibles errores
-   Estructurar el programa a criterio propio
    '''
from clase_evento import *    

class GestorEvento:
    def __init__(self):
        self.lista_eventos : list[Evento] = []
        self.lista_nombres = []
        self.organizadores = {
    "FA": "familia", 
    "AM": "amigos",
    "PR": "propio"
    }
        
    #Opcion 1
    def crear_evento(self):
        nombre = self.validar_nombre()
        fecha = self.validar_fecha()
        hora = input("Introduzca la hora del evento (hh:mm): ")
        lugar = input("Introduzca el lugar del evento: ")
        tipo = self.elegir_tipo()
        if tipo == Evento:
            evento = tipo(nombre, fecha, hora, lugar)
            self.lista_eventos.append(evento)
        elif tipo == EventoPersonal:
            organizador = self.validar_organizador()
            evento = tipo(nombre, fecha, hora, lugar, organizador)
            self.lista_eventos.append(evento)
        else:
            obligatorio = pedir_bool('¿Es obligatorio?: ')
            evento = tipo(nombre, fecha, hora, lugar, obligatorio)
            self.lista_eventos.append(evento)
            
        self.guardar_evento(evento)
            
    def guardar_evento(self, evento):
        with open('lista_eventos.txt', 'a') as f:
            f.write(f'  {evento.nombre_evento} - {evento.fecha} - {evento.hora} - {evento.lugar} - {evento.obtener_tipo_evento()}\n')
            print('Evento guardado')
                
        
    def validar_nombre(self):
        while True:
            nombre = pedir_str("Introduzca el nombre del evento: ").lower().capitalize()
            if nombre in self.lista_nombres:
                print("El nombre del evento ya existe")
            else:
                self.lista_nombres.append(nombre)
                print("Nombre del evento seteado")
                return nombre

    def validar_fecha(self):
        while True:
            fecha = pedir_str("Introduzca la fecha del evento (dd/mm/yyyy): ")
            if len(fecha) == 10:
                return fecha
            else:
                print("Fecha no válida")
                
    def elegir_tipo(self):
        tipos = {'evento': Evento, 
                        'personal': EventoPersonal,
                        'laboral': EventoLaboral}
        while True:
            print('Tipos de eventos:')
            for i in tipos:
                print(i, end = ' - ')
            
            tipo = input('inserte el tipo elegido: ')
            
            for i in tipos.keys():
                if tipo == i:
                    print(f'El tipo de evento {tipo} fue encontrado')
                    return tipos[tipo]
                
            print(f'El tipo de evento {tipo} no existe')
            
    def validar_organizador(self):
        print(f'Organizadores:')
        for organiza in self.organizadores:
            print(organiza, end = ' - ')
        organizador = input("Introduzca el organizador: ")
        return self.organizadores.get(organizador, 'Incognito')
    
    #Opcion 2
    def leer_archivo(self):
        try:
            with open('lista_eventos.txt', 'r') as f:
                f.seek(0)
                linea = f.readline()
                while linea != '':
                    print(linea)
                    linea = f.readline()
        except Exception as e:
            print(f'Error: {e}. El archivo no existe')
                    


def pedir_int(text):
    try :
        return int(input(text))
    except Exception as e:
        print(f"Erorr: {e}. Debe ser un entero")

def pedir_str(text):
    try :
        return str(input(text))
    except Exception as e:
        print(f"Erorr: {e}. Debe ser un string")
        
def pedir_float(text):
    try :
        return float(input(text))
    except Exception as e:
        print(f"Erorr: {e}. Debe ser un float")
        
def pedir_bool(text):
    while True:
        decision = input(f'{text}, (Si o No): ').lower()
        if decision == 'si':
            return True
        elif decision == 'no':
            return False
        else:
            print('Opcion incorrecta')
        
        