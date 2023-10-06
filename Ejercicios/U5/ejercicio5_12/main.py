datos = {}
def pedir_data():
  nombre = input("Ingrese su nombre: ")
  edad = int(input("Ingrese su edad: "))
  direccion = input('Ingrese su dirección: ')
  telefono = int(input('Ingrese su número de teléfono: '))
  datos.update({"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono})
  print(f"""
        Nombre: {datos.get('nombre')}
        Edad: {datos.get('edad')}
        Dirección: {datos.get('direccion')}
        Teléfono: {datos.get('telefono')}
        """)
  
pedir_data()