monedas = {
  "Peso":"$",
  "Dolar": "USD",
  "Euro":  "€"
}

def simbolo():

  moneda = input("Introduce una moneda: ").capitalize()
  if moneda in monedas:
    print(f"Moneda: {monedas[moneda]}")
  else:
    print("Moneda no válida")
    
simbolo()