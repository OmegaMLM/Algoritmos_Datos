'''
Ejercicio 3.21
El programa debe:

Pedir al usuario una palabra
Verificar que sea una palabra y no un numero
Mostrar por pantalla las letras una a una
No producir errores
'''

#Init
palabra = None
palabra_espacios = None
#Proceso


while True:
  palabra = input('Ingrese una palabra: ')
  palabra_espacios = palabra.replace(" ", "")
  
  if palabra_espacios.isalpha():
    break
  else:
    print('Ingrese una palabra sin numeros.')
  
for letra in palabra:
  print(letra)