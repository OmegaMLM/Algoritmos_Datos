#Init
dinero_actual = None
dinero_dolares = None
insumo = None
insumo_dolares = None
comprable = None

#Input
dinero_actual = float(input('Ingrese el dinero actual: '))
insumo = float(input('Ingrese el precio del insumo a comprar: '))

#Proceso
insumo_dolares = insumo / 735
dinero_dolares = dinero_actual / 735
comprable = insumo_dolares < dinero_dolares

#Out
print(f"El insumo es comprable? {comprable}")

