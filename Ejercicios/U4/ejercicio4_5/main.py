from auntentication import user_autentication
from utils import menu
def main():
  '''
  Inicio del programa
  '''
  while True:
    ingreso = user_autentication()
    menu(ingreso)

if __name__ == "__main__":
  main()
  