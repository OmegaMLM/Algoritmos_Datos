'''
Ejercicio 3.17
El programa debe:

Preguntar al usuario por una frase y una letra
mostrar por pantalla el número de veces que aparece la letra en la frase.
'''

#init
contador = 0

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

#Bucle
for i in frase:
  if i == letra:
    contador += 1

print(f'Cantidad de veces de la letra: {contador}')