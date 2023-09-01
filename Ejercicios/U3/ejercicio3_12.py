'''
Ejercicio 3.14
El programa debe:

pedir al usuario un número entero del 1 al 9 y muestrar por pantalla la tabla del numero (del 1 al 10).
no debe generar errores
'''   

#init
numero = None
contador = 0
rango = True

#Process
while rango:
  try:
      numero = int(input('Ingrese un numero entre el 1 al 9: '))
      if numero >= 1 and numero <= 9:
        rango = False
        while contador <= 10:
          print(f'{numero} x {contador} = {contador*numero}')
          contador += 1
  except Exception as error:
    print(f'Error: {error}. No es un numero valido')