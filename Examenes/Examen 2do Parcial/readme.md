'''

---

MATERIA: Algoritmos y Estructuras de Datos 1
EXAMEN: IEFI
APELLIDO Y NOMBRE: Marchesin Mateo
DNI: 43605672
CARRERA: Analista en Sistema
AÑO: 2023
Se sube al classroom en una carpeta comprimida [Apellido,Nombre Rec_2_examen]

---

Ítems a evaluar:

1.  Contenidos de la materia
2.  Requerimientos y comprensión de consignas
3.  Estructura (modularización), legibilidad y comentarios del código.

¡Cualquier duda con el enunciado consultar al docente!

---

ENUNCIADO: "Programa de Agenda"

Introducción:
El siguiente programa consiste en un software que simule una agenda personal.
El programa debe permitir agregar y quitar Eventos al sistema, como también gestionar datos del evento (Fecha, Hora, Lugar).

Requerimientos:
El programa debe:

-   Contar con una Clase Evento con los atributos (nombre_evento (único), fecha, hora, lugar)
-   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo más: - EventoPersonal (Atributo: organizador (nombre de la grupo que organiza)) - EventoLaboral (Atributo: obligatorio "True o False" (por defecto = True))
-   Se deben crear 4 métodos para la clase padre Evento (que heredaran las clases hijas): 1. Mostrar información: Que indique el nombre_evento, fecha y lugar del evento 2. Obtener tipo de evento (tipo de clases heredadas o padre) 3. Setear Fecha y Hora (Setearán la Fecha y Hora en una misma función) 4. Setear lugar (Setear el lugar)

-   Se debe crear una clase GestorEvento que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de un evento y guárdalos en una lista de eventos.
        1.1) Se debe verificar que tipo de instancia de evento a crear y los parámetros. IMPORTANTE!: clase hijas verificar y pedir parámetros - nombre_evento: debe ser único. Ayuda: verificar que ningun objet de la lista tenga ese nombre - Fecha: formato (dd/mm/yyyy) -> verificar unicamente que la longitud del string sea 10. Ayuda!: Metodo len() - Hora: formato (hh:mm) -> no es necesario verificar - Lugar: sin formato especifico -> no es necesario verificar
        1.2) Al crear un evento es necesario logearlo (Escribir en una línea nueva: nombre_evento-Fecha-Hora-Lugar-Tipo_de_evento(tipo de clase))
        en un archivo llamado lista_eventos.txt (Crear función en el mismo gestor). IMPORTANTE!: verificar permisos
        1.3) En caso que la instancia del evento sea EventoPersonal. - Para el organizador, el usuario debe elegir a través de una clave (mostradas por el programa)
        desde un diccionario de organizadores. - En caso que no exista el organizador deseado debe ser "incognito" (AYUDA: Funcion get de diccionarios)
    2.  Listar eventos disponibles, leyendo la lista_evetos.txt. IMPORTANTE!: Leer el archivo, no la lista.

-   Se deben crear los métodos correspondientes para las funciones del menú en las clases correspondientes
-   Gestionar posibles errores
-   Estructurar el programa a criterio propio
    '''
