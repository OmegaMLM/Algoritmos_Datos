#Init
edad = 0
anios_trabajados = 0
anios_faltan = 0
anios_jubilacion = 0

#Input
edad = int(input('Ingrese la edad: '))
anios_trabajados = int(input('Ingrese los años: '))

#Proceso
anios_faltan = 30 - anios_trabajados
anios_jubilacion = edad + anios_faltan

#Out
print(f'Le falta un total de {anios_faltan} para jubilarse.')
print(f'La edad a la que se jubilaria es: {anios_jubilacion}')
