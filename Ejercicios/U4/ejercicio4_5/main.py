from auntentication import user_autentication
from utils import menu
def main():
  ingreso = user_autentication()
  menu(ingreso)

if __name__ == "__main__":
  main()
  