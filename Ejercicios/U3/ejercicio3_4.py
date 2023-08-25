'''
Ejercicio 3.4
El programa debe :

Almacenar una variable contraseña con una contraseña
Preguntar al usuario por la contraseña e imprimir por pantalla si la contraseña introducida por el usuario coincide o no con la variable IMPORTANTE: sin tener en cuenta mayúsculas y minúsculas.(metodos string)
no debe generar errores
'''

# init
contrasena = 'hola123'
contrasena_usuario = None

# input
contrasena_usuario = input("Introduce una contraseña: ")
contrasena_usuario = contrasena_usuario.lower()
# logic
if contrasena == contrasena_usuario:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
