from prettytable import PrettyTable

lista_materias = ["matematica", "lengua", "biologia"]

def pedir_int(texto):
  while True:
    try:
      numero = int(input(texto))
      return numero
    except:
      print("Error. Ingrese un dato valido")

def pedir_float(texto):
  while True:
    try:
      numero = float(input(texto))
      return numero
    except:
      print("Error. Ingrese un dato valido")
      
def pedir_str(texto):
  string = input(texto)
  return string

#Nombre - Edad - Mail
lista_de_alumnos=[[],[],[]]


# Opcion 1
def print_lista():
  table = PrettyTable()
  table.add_column('Nombre', lista_de_alumnos[0])
  table.add_column('Edad', lista_de_alumnos[1])
  table.add_column('Mail', lista_de_alumnos[2])
  print(table)
  
# Opcion 2
def add_alumno():
  nombre = pedir_str("Ingrese el nombre del alumno: ").lower().capitalize()
  if nombre in lista_de_alumnos[0]:
    print(f"El nombre {nombre} ya existe")
    return
  else:
    print(f'El nombre {nombre} no existe')
    print("Nombre agregado")
    lista_de_alumnos[0].append(nombre)
  while True:
    edad = pedir_int("Ingrese la edad del alumno (Entre 10 y 18): ")
    if 10 <= edad <= 18:
      lista_de_alumnos[1].append(edad)
      print('Edad agregada')
      break
    else:
      print("Edad no válida")
  while True:
    email = pedir_str("Ingrese el mail del alumno: ").lower()
    if '@' in email:
      lista_de_alumnos[2].append(email)
      print('Mail agregado')
      break
    else:
      print("Mail no válido")

#Opcion 3
def edit_edad():
  try:
    nombre = pedir_str("Introduzca el nombre del alumno: ").lower().capitalize()
    indice = lista_de_alumnos[0].index(nombre)
    print(f"Alumno encontrado: {lista_de_alumnos[0][indice]}, Edad actual: {lista_de_alumnos[1][indice]}")
    while True:
      nueva_edad = pedir_int("Introduzca la nueva edad: ")
      if nueva_edad >= 10 and nueva_edad <= 18:
        lista_de_alumnos[1][indice] = nueva_edad
        print("Edad cambiada")
        break
      else:
        print("Edad no válida")
  except Exception as error:
    print(f"Error: {error}. Alumno no encontrado")
    
#Opcion 4
def print_materias():
  table = PrettyTable()
  table.add_column('Materias', lista_materias)
  print(table)

#Opcion 5
def add_materias():
  materia = pedir_str("Introduzca la materia: ").lower()
  if materia in lista_materias:
    print(f"La materia {materia} ya existe")
    return
  else:
    print(f'La materia {materia} no existe')
    print("Materia agregada")
    lista_materias.append(materia)
