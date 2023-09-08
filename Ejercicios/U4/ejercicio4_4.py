'''
Ejercicio 4.4 (Conversor de unidades)
El programa debe:

Contar con 4 funciones:
Conversor de Grados Celcius a Fahrenheit(temperatura en °C).(buscar regla)
Conversor de cm3 a litros (cantidad de cm3)
Conversor de litros a cm3 (cantidad de litros)
Pesos a Dolares (pesos)
Contar con un menu donde debe pedir al usuario que operacion realizar
Pedir los parametros y devolver el resultado al usuario
Gestionar posibles errores
'''

def grados():
  celcius = 0
  fahren = 0
  
  while True:
    try:
      celcius = float(input('Ingrese los grados Celcius a convertir: '))
      print( f'La cantidad de grados son: {(round(celcius * 9/5) + 32)}')
      break
    except:
      print('Introduzca un numero valido.')
      
def cm3():
  while True:
    try:
      litros = float(input('Ingrese la cantidad de litros a convertir: '))
      print( f'La cantidad de cm3 son: {round(litros * 1000)}')
      break
    except:
      print('Introduzca un numero valido.')
    
def litros():
  while True:
    try:
      cm3 = float(input('Ingrese la cantidad de cm3 a convertir: '))
      print( f'La cantidad de litros son: {round(cm3 / 1000)}')
      break
    except:
      print('Introduzca un numero valido.')
      
def pesos():
  while True:
    try:
      pesos = float(input('Introduzca la cantidad de pesos a convertir: '))
      print(f'La cantidad de dolares son: {round(pesos * 700, 2)}')
      break
    except:
      print('Introduzca un numero valido.')
      
#Init
opciones = 0      

while True:
  try:
    print('''
          Opciones:
          1 - Conversor de Celcius a Fahrenheit.
          2 - Conversor de cm3 a Litros.
          3 - Conversor de Litros a cm3.
          4 - Conversor de Pesos a Dolares.
          5 - Salir.
          ''')
    
    opcion = int(input('Introduzca una opcion:'))
    
    match opcion:
      
      case 1:
        grados()
      
      case 2:
        cm3()
      
      case 3:
        litros()
        
      case 4:
        pesos()
        
      case 5:
        print('Saliendo...')
        break
      case _:
        print('Opcion incorrecta.')  
    
  except:
    print('Opcion Invalida')