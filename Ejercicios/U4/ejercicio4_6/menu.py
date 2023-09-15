from utils import *

def menu():
  while True:
    try:
      print('''
            --- Opciones ---
              1. Ver menu de productos
              2. Comprar un producto
                - Debito
                - Credito 10% de recargo
                - Efectivo 10% de rebaja
              3. Agregar stock
              4. Cambiar precio
              5. Salir
            ''')
      
      opcion = int(input('Ingrese una opcion: '))
      
      match opcion:
        case 1:
          product_menu()
        case 2:
          producto = product()
          metodo = metod()
          pay(metodo, producto)
        case 3:
          add_stock()
        case 4:
          change_price()
        case 5:
          print('Saliendo...')
          break
        case _:
          print('Ingrese una opcion valida.')
        
    except Exception as e:
      print(f'Error: {e}. Ingrese una opcion valida.')