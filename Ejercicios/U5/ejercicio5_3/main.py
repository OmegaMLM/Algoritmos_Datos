"""##
**Ejercicio 5.3**
Crear una funcion que debe:

*    Pedir al usuario una palabra o una frase
*    Indicar si esta se trata de un palindromo (ej: reconocer, neuquen, amor a roma)
*    No deben aparecer y se deben tener en cuenta todos los posibles errores

"""
def pedir_palabra():
  palabra = input("Ingrese una palabra: ")
  if palabra.isalpha():
    return palabra
  else:
    print("Error. Ingrese un dato valido")
def main():
  palabra = pedir_palabra()
  palabra = list(palabra)
  palabra_reves = palabra.copy()
  palabra_reves.reverse()
  if palabra == palabra_reves:
    print("Es palindromo")
  else:
    print("No es palindromo")
if __name__ == "__main__":
  main()