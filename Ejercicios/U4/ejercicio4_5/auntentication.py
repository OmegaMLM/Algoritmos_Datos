def user_autentication():
  user = 'mateo'
  contrasena = '1234'
  contrasena_user = ''  
  name_user = ''
  
  # Cambiar esto por un for ESTA HORRIBLE
  for i in range(3):

    name_user = input('Ingrese el usuario: ')
    contrasena_user = input('Ingrese la contrasena: ')
    if name_user == user and contrasena_user == contrasena:
      print('Usuario y contrena correctos')
      print('Entrando...')
      return True
    
    else:
      print(f'Usuario y/o contrasena incorrecta. Le quedan {2 - i} intentos.')
      
      
  print('Intentos agotados.')
  print('Saliendo')
  return False
