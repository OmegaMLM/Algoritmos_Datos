'''
Ejercicio 3.12
El programa debe:

pedir al usuario una palabra
pedir un numero al usuario
mostrar la palabra por pantalla la cantidad de veces que diga el numero
no debe generar errores
'''

#init
palabra = None
numero = None
contador = 0
error = True
#Process
while error:    
    try:
      palabra = input("Ingrese una palabra: ")
      numero = int(input("Ingrese un numero: "))
      error = False
      while contador < numero:
          print(palabra)
          contador += 1

    except ValueError as e:
      print(f"Error{e}. Ingrese un dato valido")
