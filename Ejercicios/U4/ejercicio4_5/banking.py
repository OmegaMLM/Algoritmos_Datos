def consult_balance():
  print(saldo)

def insert_money():
  while True:
    try:
      saldo += int(input('Ingrese la cantidad de dinero a ingresar: '))
      break
    except:
      print('Ingrese un numero valido.')
def extract_money():
  while True:
    try:
      saldo -= int(input('Ingrese la cantidad de dinero a extraer: '))
      break
    except:
      print('Ingrese un numero valido.')
