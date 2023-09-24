from utility import add_stock, consult_stock, delete_stock
from prettytable import PrettyTable
from PyInquirer import *
def menu():
  while True:
    try:
      questions = [
        {
          'type': 'list',
          'name': 'opcion',
          'message': 'Que desea hacer?',
          'choices': [
            '1. Ver menu de productos',
            '2. Comprar un producto',
            '3. Agregar stock',
            '4. Salir'
          ]
        }
      ]
      answers = prompt(questions)
      opcion = answers['opcion']
      print(f"Opcion seleccionada: {opcion}")
      
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