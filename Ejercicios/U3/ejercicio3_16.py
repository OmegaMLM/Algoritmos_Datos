'''
El programa debe:
  - mostrar el eco de todo lo que el usuario introduzca hasta que el usuario escriba
  "Salir" que terminara.
  - Si el usuario escribe "Hola" o "Chau" que no se haga el eco.
'''

#init
eco = None

#Process
while eco!= "salir":
  eco = input("Escriba una palabra: ")
  eco = eco.lower()
  if eco == "hola" or eco == "chau":
    continue
  else:
    print(f'Eco: {eco}')