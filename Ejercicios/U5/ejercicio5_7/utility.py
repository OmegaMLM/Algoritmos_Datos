"""
  ##**Ejercicio 5.7 (Estadisiticas)**
El programa debe:
*   Simular un programa que calcule estadisticas
*   Pedir al usuario una serie de numeros enteros el 1 al 10 (verificar) y guardarlos en una lista, hasta que el usuario ingrese "fin"
*   Luego mostrar un menu con 4 opciones
  1.  Calcular promedio
  2.  Verificar cuantos numeros son menores que el numero indicado por el usuario
  3.  Verificar cuantos numeros son mayores o igual que el numero indicado por el usuario
  4.  Verificar si un numero que desee el usuario esta en la lista
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
"""
  
  
lista = []
def pedir_int(texto):
  while True:
    try:
      numero = int(input(f"{texto}: "))
      return numero
    except Exception as error:
      print(f"Error: {error}. Ingrese un dato valido")
        
        
def pedir_str(texto):
  string = input(f"{texto}: ")
  return string



def crear_lista():
  while True:
    try:
      numero = pedir_str("Ingrese un numero del 1 al 10. Fin para terminar la carga ").lower()
      if numero == "fin":
        print('La lista creada es: ', lista)
        break
      
      elif numero.isnumeric():
        numero = int(numero)
        if numero < 11 and numero > 0:
          lista.append(numero)
        else:
          print("Error. Ingrese un numero entre el 1 y el 10")
        
      else:
        print('Introduzca un numero')
    except Exception as error:
      print(f"Error: {error}. Ingrese un dato valido")
      

def cal_prom():
  promedio = sum(lista) / len(lista)
  print(f"El promedio de la lista es: {promedio}")
  
def num_menor():
  menores = 0
  menor = pedir_int('Ingrese el numero a comparar: ')
  for i in range(len(lista)):
    if lista[i] < menor:
      menores += 1
  print(f"La cantidad de numeros menores son: {menores}")

def num_mayor():
  mayores = 0
  mayor = pedir_int('Ingrese el numero a comparar')
  for i in range(len(lista)):
    if lista[i] >= mayor:
      mayores += 1
  print(f"La cantidad de numeros mayores o iguales son: {mayores}")

def search_num():
  num = pedir_int('Ingrese el numero a buscar')
  if num in lista:
    print(f"El numero {num} esta en la lista")
  else:
    print(f"El numero {num} no esta en la lista")

def mostrar_lista():
  if len(lista) > 0:
    print(f'La lista es: {lista}')
  else:
    print('La lista esta vacia')
