''' 
Ejercicio 4.2 (Mediciones)
El programa debe:

Contar con 4 funciones (calcular Area (cuadrado), calcular Perimetro(cuadrado),calcular Area (circulo), calcular Perimetro(circulo))
Contar con un menu donde debe pedir al usuario que operacion realizar
Pedir los dos parametros y devolver el resultado al usuario
Gestionar posibles errores
'''
import math


#def

def areacuad(num1):
  return num1**2

def perimetrocuad(lado1):
  return lado1*4

def areacirc(diametro):
  return ((diametro/2) **2) * math.pi


def perimetrocircu(diametro):
  return 2*math.pi*(diametro/2)

def pedirnum(text1):
  while True:
    try:
      num1 = float(input(text1))
      return num1
    except:
      print('Error')
  
  


#Init

while True:

  try:
    print('''Introduzca una opcion:
            1 - Area cuadrado.
            2 - Perimetro cuadrado.
            3 - Area circulo.
            4 - Perimetro circulo.
            5 - Salir.
          ''')
    opcion = int(input('Introduzca una opcion: '))
    
    match opcion:
      
      case 1:
        num1 = pedirnum('Introduzca el lado: ')
        print(f'El area del cuadrado es: {areacuad(num1)}')
        
      case 2:
        num1 = pedirnum('Introduzca el lado: ')
        print(f'El perimetro del cuadrado es: {perimetrocuad(num1)}')
        
      case 3:
        num1 = pedirnum('Introduzca el diametro: ')
        print(f'El area del circulo es: {areacirc(num1)}')
        
      case 4:
        num1 = pedirnum('Introduzca el diametro: ')
        print(f'El perimetro del circulo es: {perimetrocircu(num1)}')
      
      case 5:
        print('Saliendo...')
        break
      
      case _:
        print('Opcion incorrecta')
        
  except:
    print('Opcion invalida.')
