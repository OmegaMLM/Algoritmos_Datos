from utility import *

def menu():
  crear_lista()
  while True:
    try:
      print('''
            --- Opciones ---
              1. Ver lista
              2. Calcular Promedio
              3. Ver cantidad de numeros menor que el numero ingresado
              4. Ver cantidad de numeros mayores o iguales que el numero ingresado
              5. Buscar un numero
              6. Salir
            ''')
      
      opcion = int(input('Ingrese una opcion: '))
      
      match opcion:
        case 1:
          mostrar_lista()
        case 2:
          cal_prom()
        case 3:
          num_menor()
        case 4:
          num_mayor()
        case 5:
          search_num()
        case 6:
          print('Saliendo...')
          break
        case _:
          print('Introduzca una opcion valida.')
    
    except Exception as error:
      print(f'Error: {error}. Introduzca una opcion valida.')