'''
Ejercicio 3.6:
Pedir a un usuario la temperatura (castear)
Determinar si con esa temperatura una persona tiene fiebre, esta congelado o sano.
fiebre : 37.5 y 40 grados)
si esta congelado (menor de 20°)
sino esta sano
IMPORTANTE!: No tienen que aparecer errores!
'''

# init
temperatura = None

# Process/Input/Out
try:
    temperatura = float(input("Ingrese la temperatura: "))

    if temperatura < 20:
        print("Esta congelado")
    elif temperatura >= 37.5 and temperatura <= 40:
        print("Tiene fiebre")
    elif temperatura > 40:
        print("Esta muriendo")
    else:
        print("Esta sano")

# Error
except Exception as e:
    print(f"Ingreso de temperatura incorrecto. Error: {e}")

# Finally
finally:
    print("Fin del programa")
