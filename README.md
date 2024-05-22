# Desafío - Registro de cursos

En este desafío, se desarrollará un modelo simplificado para la administración de cursos de una institución educacional. Esto implicará la creación de un modelo de datos basado en un diagrama de entidad-relación que se adjunta, así como la implementación de funcionalidades básicas para operar sobre los datos ingresados.

## Modelo de datos

El modelo de datos incluirá entidades para representar cursos, profesores, estudiantes y direcciones. Se establecerán relaciones muchos a muchos entre cursos y profesores, así como entre estudiantes y cursos. La relación de estudiante con dirección es de uno a uno.

## Funcionalidades implementadas

En el archivo `services.py`, se han desarrollado las siguientes funciones para operar sobre el modelo de datos:

- `crear_curso`: Permite crear un nuevo curso en la base de datos.
- `crear_profesor`: Crea un nuevo profesor en la base de datos.
- `crear_estudiante`: Crea un nuevo estudiante en la base de datos y lo asocia a un curso existente.
- `crear_direccion`: Crea una nueva dirección asociada a un estudiante.
- `obtener_estudiante`: Obtiene un estudiante de la base de datos utilizando su RUT.
- `obtener_profesor`: Obtiene un profesor de la base de datos utilizando su RUT.
- `obtener_curso`: Obtiene un curso de la base de datos utilizando su código.
- `agregar_profesor_a_curso`: Agrega un profesor a un curso existente.
- `agregar_cursos_a_estudiante`: Agrega un curso a un estudiante existente.
- `imprimir_estudiante_cursos`: Imprime los estudiantes y los cursos a los que están inscritos.

## Pruebas y Capturas de pantalla

Se han realizado pruebas exhaustivas de las funcionalidades implementadas y se han capturado pantallazos del proceso. Estas capturas se encuentran en la carpeta `screenshots` en la carpeta raíz del proyecto. El modelo de entidades también se puede encontrar en esta carpeta.

## Archivos adjuntos

Se adjuntan archivos en formato JSON para poblar las tablas de la base de datos utilizando el comando `python manage.py loaddata [nombre_archivo]`.

## Autor

Jose Contreras Stoltze
