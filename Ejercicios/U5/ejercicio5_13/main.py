verduleria = {
  "fruta": {
    "manzana": 80,
    "banana": 50,
    "pera": 60,
    "naranja": 30
  },
  "verdura": {
    "cebolla": 20,
    "zanahoria": 50,
    "tomate": 30,
    "lechuga": 10
  }
}

def pedir_fruta():
  eleccion = input("¿Que desea comprar? (fruta/verdura): ")
  if eleccion == "fruta":
    
    fruta = input("¿Que fruta desea? (manzana/banana/pera/naranja): ")
    peso = int(input("¿Cuantos kg desea? "))
    total = print(f"El total a pagar es: {verduleria['fruta'][fruta] * peso}")
  
  else:
    verdura = input("¿Que verdura desea? (cebolla/zanahoria/tomate/lechuga): ")
    peso = int(input("¿Cuantos kg desea? "))
    total = print(f"El total a pagar es: {verduleria['verdura'][verdura] * peso}")
    
pedir_fruta()