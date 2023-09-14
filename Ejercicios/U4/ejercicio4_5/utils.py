from banking import consult_balance, extract_money, insert_money

def menu(ingress):
  '''
  Menu y llamada a funciones
  '''
  opcion = 0
  
  if ingress:
    while True:
      try:
        print('''
          Opciones:
          1 - Consultar el saldo.
          2 - Ingresar dinero.
          3 - Retirar dinero.
          4 - Salir.
          ''')
        opcion = int(input('Ingrese una opcion: '))
        
        if opcion == 1:
          consult_balance()
        elif opcion == 2:
          insert_money()
        elif opcion == 3:
          extract_money()
        elif opcion == 4:
            print('Saliendo...')
            break
        
        else:
            print('Introduzca una opcion correcta')
            
      except Exception as Error:
        print(f'Error: {Error} ingrese una opcion correcta.')
        
  else:
    print('Autenticacion erronea')
