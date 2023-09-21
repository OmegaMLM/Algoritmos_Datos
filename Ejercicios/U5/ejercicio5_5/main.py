"""##**Ejercicio 5.5**
Crear una funcion que debe:

*   Pedir al usuario una cantidad de tramos de un viaje
*   Pedir al usuario la duracion en minutos de cada tramo (usar listas)
*   Calcular el tiempo total de viaje (motrar en horas)
*   No deben aparecer y se deben tener en cuenta todos los posibles errores
"""

def pedir_int(texto):
  try:
    numero = int(input(f"{texto}: "))
    return numero
  except:
    print("Error. Ingrese un dato valido")
    
def pedir_float(texto):
  try:
    numero = float(input(f"{texto}: "))
    return numero
  except:
    print("Error. Ingrese un dato valido")
    
    
def main():
  total = 0
  duracion = []
  tramos = pedir_int("Ingrese la cantidad de tramos")
  for i in range(0, tramos):
    duracion.append(pedir_float("Ingrese los minutos del tramo"))
  
  for i in range(0, tramos):
    total += duracion[i]
  total = round(total/60, 2)
  print(f"La duracion es de: {total} horas")
  
if __name__ == "__main__":
  main()