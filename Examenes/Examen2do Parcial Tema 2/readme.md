---
MATERIA: Algoritmos y Estructuras de Datos 1
EXAMEN: 2° Examen - SIMULACRO
APELLIDO Y NOMBRE:
DNI:
CARRERA:
AÑO: 2023
Se envia mail con asunto: "[AYEDI 2023 - Apellido, Nombre - 2°Examen]"
---

Items a evaluar:

1.  Contenidos de la materia
2.  Requerimientos y comprension de consignas
3.  Estructura (modularización), legibilidad y comentarios del codigo.

¡Cualquier duda con el enunciado consultar al docente!

---

ENUNCIADO: "Programa de Gestión de una biblioteca"

Introduccion:
El siguiente programa consiste en un software de gestion de libros en una biblioteca.
El programa debe permitir agregar y quitar libros al sistema, como tambien gestionar el alquiler de estos libros.

Requerimientos:
El programa debe:

-   Contar con una Clase Libro con los atributos (Id(unico), Nombre, Autor y estado (ALQUILADO o NO ALQUILADO))
-   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo mas: - LibroNiños (Atributo: edad_minima (por defecto = 11)) - LibroIdiomas (Atributo: idioma_libro)
-   Se deben crear 4 metodos para la clase padre Libro (que heredaran las clases hijas): 1. Presentarse: Que indique el id, Nombre, autor y su estado 2. Indicar tipo de libro (tipo de clases heredadas o padre) 3. Alquilar (Cambiaran el estado del libro a ALQUILADO) 4. Devolver_alquiler (Cambiaran el estado del libro a NO ALQUILADO)

-   Se debe crear una clase GestorBiblioteca que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de libros y guardalos en una lista de libros.
        1.1) Se debe verificar que tipo de instancia de libro crear y los parametros - Id debe ser unico - Nombre y autor no es necesario verificar nada - estado debe comenzar "NO ALQUILADO"
        1.2) Al crear un libro es necesario logearlo (Escribir en una linea nueva: id-nombre-autor)
        en un archivo llamado libros.txt (Crear funcion en el mismo gestor)
        1.3) En caso que la instancia del libro sea LibroIdiomas. - El usuario debe elegir el idioma a travez de una clave (mostradas por el programa) desde un diccionario de idiomas. - En caso que no exista el idioma deseado debe ser en idioma "español" (AYUDA: Funcion get de diccionarios)
    2.  Listar libros disponibles (recorrer la lista, no el archivo)
    3.  Cambiar el estado (Alquilar o devolver) de un libro, seleccionando su id. (Hacer check correspondientes)

-   Se deben crear los metodos correspondientes para las funciones del menu en las clases correspondientes
-   Gestionar posibles errores
-   Estructurar el programa a criterio propio
