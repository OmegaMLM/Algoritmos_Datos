"""
  ##**Ejercicio 5.4**
Crear funciones que deban:

*    Pedir al usuario 5 materias (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
*    Verficiar que sea un nombre correcto
*    Almacenar los nombres en una lista
*    Mostrar las materias en orden alfabetico
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
def pedir_str(texto):
  while True:
    try:
      valor = input(texto)
      if valor.isalpha():
        return valor
      else:
        print('Ingrese una materia correcta')
    except:
      print('Ingrese un valor correcto')
  
def main():
  materias = []
  for i in range(5):
    materias.append(pedir_str('Ingrese una materia: ').lower())
  materias.sort()
  print(f"Las materias son: {materias}")

if __name__ == '__main__':
  main()