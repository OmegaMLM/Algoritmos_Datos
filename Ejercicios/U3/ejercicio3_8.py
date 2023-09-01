'''
Ejercicio 3.8 (Tarea)
El programa siguiente muestra el color obtenido al mezclar dos colores en la pantalla, siendo los 3 posibles:

Azul.
Rojo.
Verde.
'''

#init
color1 = None
color2 = None

while True:
  #input
  color1 = input('Ingrese el color Azul o Rojo: ')
  color1 = color1.lower()

  #match
  match color1:

    #rojo
    case 'rojo':
      color2 = input('Ingrese el segundo color. Verde o Azul: ')
      color2 = color2.lower()
      if color2 == 'azul':
        print('El color creado es el morado.')
        break
      elif color2 == 'verde':
            print('El color creado es amarillo.')
            break
      else:
        print('Ingreso erroneo, ingrese el color nuevamente.')

    #azul
    case 'azul':
      color2 = input('Ingrese el segundo color. Rojo o Verde: ')
      color2 = color2.lower()
      if color2 == 'rojo':
        print('El color creado es el morado.')
        break

      elif color2 == 'verde':
        print('El color creado es cyan.')
        break

      else:
        print('Ingreso erroneo, ingrese el color nuevamente.')

    #No correcto
    case _:
        print('El color ingresado no es correcto.')
