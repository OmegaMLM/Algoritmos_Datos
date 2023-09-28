from utility import add_stock, consult_stock, delete_stock
def menu():
  while True:
    try:
      print("""
            --- Inventario la Verdugod ---
            1. Agregar stock
            2. Consultar stock
            3. Eliminar stock
            4. Salir
            """)
      opcion = int(input('Ingrese una opcion: '))
      match opcion:
        case 1:
          add_stock()
        case 2:
          consult_stock()
        case 3:
          delete_stock()
        case 4:
          print('Saliendo...')
          break
        case _:
          print('Introduzca una opcion correcta.')
    except Exception as error:
        print(f"Error: {error}. Introduzca una opcion valida.")