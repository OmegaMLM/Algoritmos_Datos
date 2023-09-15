lista = [1,True, 'Fede', 4]
cantidad = 0


for i in lista:
  if str(i).isdigit():
    cantidad += 1
print(cantidad)