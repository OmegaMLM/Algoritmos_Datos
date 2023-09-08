'''
Ejercicio 4.1 (Calculadora)
El programa debe:

Contar con 4 funciones (suma, resta, división y multiplicación)
Contar con un menu donde debe pedir al usuario que operacion realizar
Pedir los dos numero para operar y devolver el resultado al usuario
Gestionar posibles errores
'''

def suma(num1, num2):

  return num1 + num2


def resta(num1, num2):
  
  return num1 - num2

def multipliacion(num1, num2):
  
  return num1 * num2

def divicion(num1, num2):
  
  return num1 / num2

def pedirnum():
  num1 = 0
  num2 = 0
  while True:
    try:
      num1 = float(input('Introduzca el primer numero: '))
      num2 = float(input('Introduzca el segundo numero: '))
      return num1, num2
    except:
      print('Introduzca un numero valido.')


#Init
opcion = 0
num1 = 0
num2 = 0
resultado = 0


while True:
  try:
    
    print('''Calculadora
      Introduzca una de las opciones: 
      1 - Suma
      2 - Resta
      3 - Multiplicacion
      4 - Divicion
      5 - Salir''')
    
    opcion = int(input('Introduzca una opcion: '))
    
    match opcion:
      case 1:
        num1, num2 = pedirnum()
        resultado = suma(num1, num2)
        print(f'El resultado es: {resultado}')
      case 2:
        num1, num2 = pedirnum()
        resultado = resta(num1, num2)
        print(f'El resultado es: {resultado}')
      case 3:
        num1, num2 = pedirnum()
        resultado = multipliacion(num1, num2)
        print(f'El resultado es: {resultado}')
      case 4:
        num1, num2 = pedirnum()
        resultado = divicion(num1, num2)
        print(f'El resultado es: {resultado}')
      case 5:
        print('Saliendo...')
        break
      
      case _:
        print('Opcion incorrecta')
  except:
    print('Opcion invalida')