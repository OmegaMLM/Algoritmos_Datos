saldo = 50000

def consult_balance():
  global saldo
  print(saldo)

def insert_money():
  global saldo
  while True:
    try:
      saldo += int(input('Ingrese la cantidad de dinero a ingresar: '))
      break
    except:
      print('Ingrese un numero valido.')
def extract_money():
  global saldo
  while True:
    try:
      saldo -= int(input('Ingrese la cantidad de dinero a extraer: '))
      break
    except:
      print('Ingrese un numero valido.')
