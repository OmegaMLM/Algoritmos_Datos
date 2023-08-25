# Init
num1 = None
num2 = None

# Input/Preceso
try:
    num1 = int(input('Introduzca el primer numero: '))
    num2 = int(input('Introduzca el segundo numero: '))
    print(f'El resultado es: {num1 + num2}')
except Exception as error:
    print(f'Error: {error}')
