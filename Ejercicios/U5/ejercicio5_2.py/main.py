"""
##**Ejercicio 5.2**
Crear una funcion que debe: (usar listas)

*    Pedir al usuario cantidad de personas
*    Pedir al usuario una a una la edad de las personas
*    Finalizado la carga de las edades debe imprimir por pantalla la edad mayor
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
def pedir_str(texto):
  string = input(f"{texto}: ")
  if texto.isalpha():
    return string
  else:
    print("Error. Ingrese un dato valido")

def pedir_int(texto):
  try:
    numero = int(input(f"{texto}: "))
    return numero
  except:
    print("Error. Ingrese un dato valido")

def main():
  edad = []
  
  personas = pedir_int("Ingrese una cantidad de personas")
  for i in range(personas):
    edad.append(pedir_int("Ingrese la edad de la persona"))
  edad.sort(reverse=True)
  print(f"La persona con mayor edad tiene: {edad[0]}")
  
if __name__ == "__main__":
  main()