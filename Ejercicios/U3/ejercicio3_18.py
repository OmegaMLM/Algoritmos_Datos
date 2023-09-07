'''
Ejercicio 3.18
El programa debe:

Pedir al usuario un número entero positivo 
y mostrar por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''

#Init
try:
  num = int(input('Ingrese un numero: '))

  for i in range(num,-1, -1 ):
    print(i)
    
except:
  print('Error')