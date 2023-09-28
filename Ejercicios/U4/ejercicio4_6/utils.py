from prettytable import PrettyTable

# Codigo, Nombre, Precio, Stock
productos = [[1,2,3], ["Maseta","Cafetera","Termo"], [300,400,500], [5,4,7]]
metodos = ["efectivo", "debito", "credito"]

def pedir_int(texto):
  while True:
    try:
      numero = int(input(f"{texto}: "))
      return numero
    except Exception as error:
      print(f"Error: {error}. Ingrese un dato valido")

def pedir_float(texto):
  while True:
    try:
      numero = float(input(f"{texto}: "))
      return numero
    except Exception as error:
      print(f"Error: {error}. Ingrese un dato valido")        
        
def pedir_str(texto):
  string = input(f"{texto}: ")
  return string

def product_menu():
  table = PrettyTable()
  table.add_column('Codigo', productos[0])
  table.add_column('Nombres', productos[1])
  table.add_column('Precios', productos[2])
  table.add_column('Stock', productos[3])
  print(table)

def metod():  
  while True:
    table = PrettyTable()
    table.field_names = ["Metodo", "Descripción"]
    table.add_row(["Efectivo", "10% Menos"])
    table.add_row(["Debito", "Mismo Precio"])
    table.add_row(["Credito", "10% Mas"])
    print(table)
    metodo = input('Ingrese el metodo de pago: ')
    metodo = metodo.lower()
    try:
      indice = metodos.index(metodo)
      print(f"Metodo elegido: {metodos[indice]}")
      return metodos[indice]
      
    except Exception as error:
      print('Ingrese un metodo valido.')
      
def pay(method, amount, stock):
  match method:
    
    case 'efectivo':
      print(f'El monto a pagar es: {amount - amount * 0.10}')
      if productos[3][stock] > 0:
        productos[3][stock] -= 1
      else:
        print('No hay stock de producto 1')
    case 'debito':
      print(f'El monto a pagar es: {amount}')
      if productos[3][stock] > 0:
        productos[3][stock] -= 1
      else:
        print('No hay stock de producto 2')
    case 'credito':
      print(f'El monto a pagar es: {amount + amount * 0.10} ')
      if productos[3][stock] > 0:
        productos[3][stock] -= 1
      else:
        print('No hay stock de producto 3')
    

def product():
  
  while True:
    try:
      codigo = pedir_int('Seleccione el codigo del producto')
      indice = productos[0].index(codigo)
      print('Producto elegido: ', productos[1][indice])
      return productos[2][indice], indice
    except Exception as error:
      print(f'Error: {error}, Codigo no encontrado.')

def add_stock():
  try:
    codigo = pedir_int('Seleccione el codigo del producto')
    indice = productos[0].index(codigo)
    print('Producto elegido: ', productos[1][indice])
    newstock = pedir_int('Ingrese el nuevo stock')
    productos[3][indice] += newstock
  except Exception as error:
    print(f'Error: {error}, Codigo no encontrado.')

def change_price():
  try:
    codigo = int(input('Seleccione el codigo del producto: '))
    indice = productos[0].index(codigo)
    print('Producto elegido: ', productos[1][indice])
    newprice = pedir_float('Ingrese el nuevo precio')
    productos[2][indice] = newprice
  
  except Exception as error:
    print(f'Error: {error}, codigo no encontrado.')
    