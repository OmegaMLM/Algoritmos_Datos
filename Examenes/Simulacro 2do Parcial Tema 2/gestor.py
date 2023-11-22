from clase_libro import *



class GestorBiblioteca:
    def __init__(self):
        self.lista_libros : list[Libro] = []
        self.lista_ids = set([])
        self.idiomas_disponibles = {
    "IN":"ingles", 
    "AL":"aleman",
    "CH":"chino"
    }
        
    #Opcion 1
    def crear_libro(self):
        id = self.validar_id()
        nombre = pedir_str('Ingrese el nombre del libro: ')
        autor = pedir_str('Ingrese el autor del libro: ')
        tipo = self.validar_tipo()
        if tipo == Libro:
            libro = tipo(id, nombre, autor)
            self.lista_libros.append(libro)
        
        elif tipo == LibroNinos:
            libro =  tipo(id, nombre, autor, estado = False,edad_minima = pedir_int('Ingrese la edad minima: '))
            self.lista_libros.append(libro)
        elif tipo == LibroIdiomas:
            libro =  tipo(id, nombre, autor, estado = False, idioma_libro = self.validar_idioma())
            self.lista_libros.append(libro)
        
        self.escribir_archivo(libro)
    def validar_id(self):
        while True:
            id = pedir_int('Ingrese el ID: ')
            if id in self.lista_ids:
                print('ID Incorrecto. El ID ya existe')
            else:
                self.lista_ids.add(id)
                return id
        
        
    def validar_tipo(self):
        tipos_libros = {'libro':Libro, 'libro de ninos':LibroNinos, 'libro de idiomas':LibroIdiomas}
        while True:
            for tipos in tipos_libros.keys():
                print(tipos, end = ' - ')
            tipo_elegido = pedir_str('Ingrese el tipo de libro: ').lower()
            if tipo_elegido in tipos_libros:
                return tipos_libros[tipo_elegido]
            else:
                print(f'El tipo de libro {tipo_elegido} no existe')
                

        
    def validar_idioma(self):
        for i in self.idiomas_disponibles.keys():
            print(i, end = ' - ')
        idioma = pedir_str('Ingrese el idioma del libro: ')
        return self.idiomas_disponibles.get(idioma, 'espanol')
    
    def escribir_archivo(self, libro):
        with open('historial_libros.txt', 'a') as archivo:
                archivo.write(f'ID: {libro.id}, Nombre: {libro.nombre}, Autor: {libro.autor}\n')       
                
    #Opcion 2
    def listar_libros(self):
        for i in self.lista_libros:
            i.presentarse()
            
    #Opcion 3
    def alquilar(self):
        if len(self.lista_libros) == 0:
            print('No hay libros para alquilar')
        else:
            while True:
                id = pedir_int('Ingrese el ID del libro: ')
                for i in self.lista_libros:
                    if i.id == id:
                        if i.estado:
                            i.devolver_alquiler()
                            return
                        else:
                            i.alquilar()
                            return
                else:
                    print('Libro no encontrado')
                    return
    
def pedir_int(text):
    while True:
        try:
            numero = int(input(text))
            return numero
        except Exception as e:
            print(f'Error: {e}. Ingrese un dato valido')
            
def pedir_float(text):
    while True:
        try:
            numero = float(input(text))
            return numero
        except Exception as e:
            print(f'Error: {e}. Ingrese un dato valido')
            
def pedir_str(text):
    while True:
        try:
            numero = str(input(text))
            return numero
        except Exception as e:
            print(f'Error: {e}. Ingrese un dato valido')
            
            