saldo = 50000

def consult_balance():
  '''
  Consulta el saldo e imprime por pantalla
  '''
  global saldo
  print(saldo)

def insert_money():
  '''
  Ingreso de dinero
  '''
  
  global saldo
  while True:
    try:
      saldo += float(input('Ingrese la cantidad de dinero a ingresar: '))
      break
    except:
      print('Ingrese un numero valido.')
def extract_money():
  '''
  Retiro de dinero
  '''
  global saldo
  while True:
    try:
      saldo -= float(input('Ingrese la cantidad de dinero a extraer: '))
      break
    except:
      print('Ingrese un numero valido.')
