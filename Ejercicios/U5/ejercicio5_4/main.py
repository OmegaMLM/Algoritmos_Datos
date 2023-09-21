def pedir_str(texto):
  while True:
      valor = input(texto)
      if valor.isalpha():
        return valor
      else:
        print('Ingrese una materia correcta')
  
def main():
  materias = []
  for i in range(5):
    materias.append(pedir_str('Ingrese una materia: ').lower())
  materias.sort()
  print(f"Las materias son: {materias}")

if __name__ == '__main__':
  main()