productname1 = 'product1'
productname2 = 'product2'
productname3 = 'product3'

productprice1 = 300
productprice2 = 400
productprice3 = 500

productcode1 = 1
productcode2 = 2
productcode3 = 3

productstock1 = 5
productstock2 = 4
productstock3 = 7

def product_menu():
  """
  Esta función permite al usuario seleccionar un producto ingresando su código. 
  El código del producto se ingresa mediante la función `input` y se convierte a un entero. 
  Luego, se comparará el código del producto con los códigos de los productos existentes (`productcode1`, `productcode2` y `productcode3`).
  Si el código ingresado coincide con alguno de los códigos de producto, se imprime el nombre del producto correspondiente y se retorna su precio.
  Si el código ingresado no coincide con ninguno de los códigos de producto, se imprime un mensaje de error.
  Si ocurre alguna excepción durante la ejecución del código, se captura y se imprime un mensaje de error.

  Parámetros:
    No recibe ningún parámetro.

  Retorna:
    El precio del producto seleccionado, o None si no se seleccionó ningún producto válido.
  """
  print(f'''
Codigo  Nombre Precio Stock
  {productcode1}. {productname1} - {productprice1} - {productstock1}
  {productcode2}. {productname2} - {productprice2} - {productstock2}
  {productcode3}. {productname3} - {productprice3} - {productstock3}''')

def metod():
  """
  Función que muestra un menú de métodos de pago y solicita al usuario que ingrese un método de pago válido. 
  Los métodos de pago válidos son: 'efectivo', 'debito' y 'credito'. 
  Si se ingresa un método de pago válido, se muestra un mensaje confirmando el método elegido y se retorna el método. 
  Si se ingresa un método de pago inválido, se muestra un mensaje de error y se solicita nuevamente al usuario que ingrese un método válido.

  Parámetros:
    No recibe ningún parámetro.

  Retorna:
    Una cadena de texto que representa el método de pago elegido por el usuario.

  """
  
  while True:
    print('''
          ---Metodos de pago ---
              Efectivo
              Debito
              Credito
          ''')
    metodo = input('Ingrese el metodo de pago: ')
    metodo = metodo.lower()
    if metodo == 'efectivo' or metodo == 'debito' or metodo == 'credito':
      print(f'Metodo elegido: {metodo}')
      return metodo
    else:
      print('Ingrese un metodo valido.')
      
def pay(method, amount):
  """
  Realiza el pago de una compra según el método de pago y el monto proporcionados.

  Args:
      method (str): El método de pago utilizado. Puede ser "efectivo", "debito" o "credito".
      amount (float): El monto total de la compra.
  """
  
  global productstock1
  global productstock2
  global productstock3
  match method:
    case 'efectivo':
      print(f'El monto a pagar es: {amount - amount * 0.10}')
      if productstock1 > 0:
        productstock1 -= 1
      else:
        print('No hay stock de producto 1')
    case 'debito':
      print(f'El monto a pagar es: {amount}')
      if productstock2 > 0:
        productstock2 -= 1
      else:
        print('No hay stock de producto 2')
    case 'credito':
      print(f'El monto a pagar es: {amount + amount * 0.10} ')
      if productstock3 > 0:
        productstock3 -= 1
      else:
        print('No hay stock de producto 3')
    

def product():
  """
  Esta función permite al usuario seleccionar un producto ingresando su código. 
  El código del producto se ingresa mediante la función `input` y se convierte a un entero. 
  Luego, se comparará el código del producto con los códigos de los productos existentes (`productcode1`, `productcode2` y `productcode3`).
  Si el código ingresado coincide con alguno de los códigos de producto, se imprime el nombre del producto correspondiente y se retorna su precio.
  Si el código ingresado no coincide con ninguno de los códigos de producto, se imprime un mensaje de error.
  Si ocurre alguna excepción durante la ejecución del código, se captura y se imprime un mensaje de error.

  Parámetros:
    No recibe ningún parámetro.

  Retorna:
    El precio del producto seleccionado, o None si no se seleccionó ningún producto válido.
  """
  
  while True:
    try:
      product = int(input('Seleccione el codigo del producto: '))
      if product == productcode1:
        print('Producto elegido: ', productname1)
        return productprice1
      elif product == productcode2:
        print('Producto elegido: ', productname2)
        return productprice2
      elif product == productcode3:
        print('Producto elegido: ', productname3)
        return productprice3
      else:
        print('Ingrese un producto valido.')
    except Exception as error:
      print(f'Error: {error}, Ingrese un codigo valido.')

def add_stock():
  """
  Esta función agrega stock a los productos existentes en base a la cantidad ingresada por el usuario.

  Parámetros:
    No recibe ningún parámetro.

  Retorna:
    No retorna ningún valor.
  """
  
  global productstock1
  global productstock2
  global productstock3
  
  cantidad = 0
  while True:
    try:
      product = int(input('Seleccione el codigo del producto: '))
      cantidad = int(input('Ingrese la cantidad a agregar: '))
      if product == productcode1:
        print('Producto elegido: ', productname1)
        productstock1 += cantidad
        print('Nuevo stock: ', productstock1)
        break
      elif product == productcode2:
        print('Producto elegido: ', productname2)
        productstock2 += cantidad
        print('Nuevo stock: ', productstock2)
        break
      elif product == productcode3:
        print('Producto elegido: ', productname3)
        productstock3 += cantidad
        print('Nuevo stock: ', productstock3)
        break
      else:
        print('Ingrese un producto valido.')
    except Exception as error:
      print(f'Error: {error}, Ingrese un codigo valido.')
      
      
def change_price():
  """
  Función para cambiar el precio de un producto.

  Parámetros:
  - No tiene parámetros.

  Tipo de retorno:
  - No retorna ningún valor.
  """
  
  global productprice1
  global productprice2
  global productprice3
  
  cantidad = 0
  while True:
    try:
      product = int(input('Seleccione el codigo del producto: '))
      precio = int(input('Ingrese el precio a modificar: '))
      if product == productcode1:
        print('Producto elegido: ', productname1)
        productprice1 = precio
        print('Nuevo precio: ', productprice1)
        break
      elif product == productcode2:
        print('Producto elegido: ', productname2)
        productstock2 = precio
        print('Nuevo precio: ', productprice2)
        break
      elif product == productcode3:
        print('Producto elegido: ', productname3)
        productprice3 = precio
        print('Nuevo precio: ', productprice3)
        break
      else:
        print('Ingrese un producto valido.')
    except Exception as error:
      print(f'Error: {error}, Ingrese un codigo valido.')
      
pay('credito', 100)