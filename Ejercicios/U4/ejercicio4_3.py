'''
Ejercicio 4.3 (Palabras)
El programa debe:

Contar con 3 funciones:
Contador de letras (letra,palabra): Debe contar la cantidad de letras que tiene una palabra o frase (Ambos parametros)
Comparador de palabras (palabra1 vs palabra2): debe comparar que palabra tiene mas letra.IMPORANTE:deben ser palabras y no frases (verificar)
Quitador de vocales(palabra a retirar las vocales): debe recibir una palabra o frase y quitar todas las vocales
Contar con un menu donde debe pedir al usuario que operacion realizar
Pedir los parametros y devolver el resultado al usuario
Gestionar posibles errores
'''

def contarletras(palabra):
  contador = 0
  
  palabra = palabra.replace(" ", "")
  for i in palabra:
    contador += 1
  print(f'Tiene {contador} letras.')

def comparador(palabra1, palabra2):
  contador1 = 0
  contador2 = 0
    
  for i in palabra1:
    contador1 += 1
  for i in palabra2:
    contador2 += 1
  
  if contador1 > contador2:
    print('La primera palabra es mas grande.')
  elif contador1 < contador2 :
    print('La segunda palabra es mas grande.')
  else:
    print('Las palabras son iguales.')
    

def sacarvocales(palabra):
  palabranovoc = ""
  
  for letra in palabra:
    if letra in 'aeiou':
      pass
    else:
      palabranovoc += letra
  print(f'La palabra sin vocales es: {palabranovoc}')
    

def verificarpal():
    while True:
      palabra1 = input('Introduzca la primera palabra: ')
      if palabra1.find(' ') >= 0:
        print('Introduzca una palabra, no una frase.')
        continue
      
      palabra2 = input('Introduzca la segunda palabra:')
      if palabra2.find(' ') >= 0:
        print('Introduzca una palabra, no una frase')
      
      else:
        return palabra1, palabra2

#Main

#Init
opcion = 0
palabra = None
while True:
  try:
    print('''
          Elija una de las opciones:
            1 - Contar letras.
            2 - Comparar palabras.
            3 - Quitar vocales.
            4 - Salir.
          ''')
    
    opcion = int(input('Ingrese una opcion: '))
    
    match opcion:
      
      case 1:
        palabra = input('Introduzca una palabra: ')
        contarletras(palabra)
        
      case 2:
        palabra1, palabra2 = verificarpal()
        comparador(palabra1, palabra2)
        
      case 3:
        palabra = input('Introduzca una palabra: ')
        sacarvocales(palabra)
        
      case 4:
        print('Saliendo...')
        break
      
      case _:
        print('Opcion incorrecta.')
  except:
    print('Ingrese una opcion valida')