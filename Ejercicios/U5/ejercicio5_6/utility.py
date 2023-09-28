from prettytable import PrettyTable


stock_frutas = [["banana", "manzanas"],[20,40]]
stock_verduras = [["zanahoria", "calabaza"], [15, 30]]

def add_stock():
  global stock_frutas
  global stock_verduras
  while True:
    try:
      tipo = int(input('Seleccione si es fruta o verdura (1 o 2 o 3 - Salir): '))
      match tipo:
        case 1:
          print("Eligio fruta")
          while True:
            try:
              nombre = input('Ingrese el nombre de la fruta: ')
              nombre = nombre.lower()
              cantidad = int(input('Ingrese la cantidad de fruta: '))
              if nombre in stock_frutas[0]:
                print('El nombre de la fruta ya existe')
                break
              else:
                print('El nombre de la fruta no existe. Añadiendo fruta')
                stock_frutas[0].append(nombre)
                stock_frutas[1].append(cantidad)
                break
            except Exception as error:
              print(f'Error: {error}. Ingrese una cantidad valida')
          
        case 2:
          print("Eligio Verdura")
          while True:
            try:
              nombre = input('Ingrese el nombre de la verdura: ')
              nombre = nombre.lower()
              cantidad = int(input('Ingrese la cantidad de verdura: '))
              if nombre in stock_verduras[0]:
                print('El nombre de la verdura ya existe')
                break
              else:
                print('El nombre de la verdura no existe. Añadiendo verdura')
                stock_verduras[0].append(nombre)
                stock_verduras[1].append(cantidad)
                break
            except Exception as error:
              print(f'Error: {error}. Ingrese una cantidad valida')
        
        case 3:
          print('Saliendo...')
          break
        case _:
          print('Error. Ingrese una opcion correcta')
    except Exception as error:
      print(f'Error: {error}. Ingrese una opcion valida')
      
def consult_stock():
  global stock_frutas
  global stock_verduras
  
  # Tabla de frutas
  table_frutas = PrettyTable()
  table_frutas.add_column('Frutas', stock_frutas[0])
  table_frutas.add_column('Stock', stock_frutas[1])
  print("Tabla de frutas")
  print(table_frutas)

  
  
  # Tabla de verduras
  table_verduras = PrettyTable()
  table_verduras.add_column('Verduras', stock_verduras[0])
  table_verduras.add_column('Stock', stock_verduras[1])
  print("\nTabla de verduras")
  print(table_verduras)

def delete_stock():
  global stock_frutas
  global stock_verduras
  while True:
    try:
      tipo = int(input('Seleccione si es fruta o verdura (1 o 2 o 3 - Salir): '))
      match tipo:
        case 1:
          print("Eligio fruta")
          fruta = input('Ingrese el nombre de la fruta a borrar: ')
          try:
            indice = stock_frutas[0].index(fruta)
            print(f'Eliminando fruta: {stock_frutas[0][indice]}')
            stock_frutas[0].pop(indice)
            stock_frutas[1].pop(indice)
          except:
            print("El nombre de la fruta no existe")
          
        case 2:
          print("Eligio verdura")
          verdura = input('Ingrese el nombre de la verdura a borrar: ')
          try:
            indice = stock_verduras[0].index(verdura)
            print(f'Eliminando fruta: {stock_verduras[0][indice]}')
            stock_verduras[0].pop(indice)
            stock_verduras[1].pop(indice)
          except:
            print("El nombre de la fruta no existe")
        case 3:
          print('Saliendo...')
          break
        case 4:
          print('Error. Ingrese una opcion correcta')
    except Exception as error:
      print(f'Error: {error}. Ingrese una opcion valida')

