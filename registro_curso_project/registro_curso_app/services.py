from .models import Profesor, Curso, Estudiante, Direccion
from registro_curso_app.models import Profesor


def crear_profesor(rut, nombre, apellido, activo, creado_por):
    """
    Crea un nuevo profesor en la base de datos.

    Args:
        rut (str): Rut del profesor.
        nombre (str): Nombre del profesor.
        apellido (str): Apellido del profesor.
        activo (boolean): Estado del profesor en el sistema.
        creado_por (str): Nombre de la persona que crea el profesor.

    Returns:
        Profesor: El objeto Profesor recién creado.
    """
    profesor = Profesor.objects.create(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        activo=activo,
        creado_por=creado_por
    )
    return profesor


def crear_curso(codigo, nombre, version):
    """
    Crea un nuevo curso en la base de datos.

    Args:
        codigo (str): Código del curso.
        nombre (str): Nombre del curso.
        version (int): Versión del curso.

    Returns:
        Curso: El objeto Curso recién creado.
    """
    curso = Curso.objects.create(
        codigo=codigo,
        nombre=nombre,
        version=version
    )
    return curso


def crear_estudiante(rut, nombre, apellido, fecha_nac, activo=None, creacion_registro=None, modificacion_registro=None, creado_por=None):
    """
    Crea un nuevo estudiante en la base de datos.

    Args:
        rut (str): Rut del estudiante.
        nombre (str): Nombre del estudiante.
        apellido (str): Apellido del estudiante.
        fecha_nac (datetime): Fecha de nacimiento del estudiante.
        creado_por (str): Nombre del usuario que creó el registro del estudiante.
        curso (Curso): Objeto Curso al que pertenece el estudiante.
        activo (bool): Estado de activación del estudiante.
        creacion_registro (date): Fecha de creación del registro del estudiante.
        modificacion_registro (date): Fecha de última modificación del registro del estudiante.

    Returns:
        Estudiante: El objeto Estudiante recién creado.
    """

    parametros = {
        'rut': rut,
        'nombre': nombre,
        'apellido': apellido,
        'fecha_nac': fecha_nac,
        'creado_por': creado_por
    }

    # Manejo de parámetros no obligatorios
    if activo is not None:
        parametros['activo'] = activo

    if creacion_registro is not None:
        parametros['creacion_registro'] = creacion_registro

    if modificacion_registro is not None:
        parametros['modificacion_registro'] = modificacion_registro

    if creado_por is not None:
        parametros['creado_por'] = creado_por

    # Crea el registro en la base de datos
    estudiante = Estudiante.objects.create(**parametros)
    return estudiante


def crear_direccion(calle, numero, comuna, ciudad, region, estudiante_id, dpto=None):
    """
    Crea una nueva dirección en la base de datos.

    Args:
        calle (str): Calle de la dirección.
        numero (str): Número de la dirección.
        comuna (str): Comuna de la dirección.
        ciudad (str): Ciudad de la dirección.
        region (str): Región de la dirección.
        estudiante_id (int): ID del estudiante asociado a la dirección.
        dpto (str, optional): Departamento de la dirección.

    Returns:
        Direccion: El objeto Direccion recién creado.
    """

    estudiante = Estudiante.objects.get(id=estudiante_id)  # Accede a la instancia del estudiante

    parametros = {
        'calle': calle,
        'numero': numero,
        'comuna': comuna,
        'ciudad': ciudad,
        'region': region,
        'estudiante': estudiante
    }

    # Manejo de parámetro no obligatorio
    if dpto is not None:
        parametros['dpto'] = dpto

    # Crea el registro en la base de datos
    direccion = Direccion.objects.create(**parametros)
    return direccion


def obtener_estudiante(rut):
    """
    Obtiene un estudiante de la base de datos usando su RUT.

    Args:
        rut (str): RUT del estudiante.

    Returns:
        Estudiante: El objeto Estudiante.
    """
    # Obtiene el estudiante ingresando su rut y lo retorna
    estudiante = Estudiante.objects.get(rut=rut)
    return estudiante


def obtener_profesor(rut):
    """
    Obtiene un profesor de la base de datos usando su RUT.

    Args:
        rut (str): RUT del profesor.

    Returns:
        Profesor: El objeto Profesor.
    """
    # Obtiene el profesor ingresando su rut y lo retorna
    profesor = Profesor.objects.get(rut=rut)
    return profesor


def obtener_curso(codigo):
    """
    Obtiene un curso de la base de datos usando su código.

    Args:
        codigo (str): Código del curso.

    Returns:
        Curso: El objeto Curso.
    """
    
    # Obtiene el curso ingresando su codigo y lo retorna
    curso = Curso.objects.get(codigo=codigo)
    return curso


def agregar_profesor_a_curso(codigo_curso, profesor_rut):
    
    """
    Agrega un profesor a un curso en la base de datos.

    Args:
        código (str): código del curso al que se añadirá el profesor.
        profesor_rut (str): RUT del profesor que se añadirá al curso.

    Returns:
        str: Mensaje indicando el resultado de la operación.
    """
    curso = obtener_curso(codigo_curso) # Obtiene el curso de acuerdo con codigo ingresado
    profesor = obtener_profesor(profesor_rut) # Obtiene el profesor de acuerdo con el rut ingresado

    # Se agrega el profesor a la tabla intermedia entre ambas entidades y se retorna un string
    curso.profesores.add(profesor)
    return f"El profesor: {profesor.rut}, {profesor.apellido}, {profesor.nombre} ha sido agregado al curso {curso.codigo} - {curso.nombre}."

def agregar_cursos_a_estudiante(codigo_curso, estudiante_rut):
    
    """
    Agrega un curso a un estudiante en la base de datos.

    Args:
        código (str): código del curso al que se añadirá el profesor.
        profesor_rut (str): RUT del profesor que se añadirá al curso.

    Returns:
        str: Mensaje indicando el resultado de la operación.
    """
    curso = obtener_curso(codigo_curso) # Obtiene el curso de acuerdo con codigo ingresado
    estudiante = obtener_estudiante(estudiante_rut) # Obtiene el estudiante de acuerdo con el rut ingresado

    # Se agrega el curso a la tabla intermedia entre ambas entidades y se retorna un string
    estudiante.cursos.add(curso)
    return f"El curso: {curso.codigo} - {curso.nombre} ha sido agregado al estudiante: {estudiante.rut}, {estudiante.nombre}, {estudiante.apellido}."


def imprimir_estudiantes_y_cursos():
    """
    Imprime los estudiantes y los cursos a los que están inscritos.
    """
    estudiantes = Estudiante.objects.all() # Obtiene todos los estudiantes

    # Itera los estudiantes imprimiendo sus datos en pantalla
    for estudiante in estudiantes:
        print(f"Estudiante: {estudiante.rut}, {estudiante.apellido}, {estudiante.nombre}")
        print("Cursos:")

        # Itera los cursos del estudiante y los imprime en pantalla
        for curso in estudiante.cursos.all():
            print(f"    - {curso.codigo} - {curso.nombre}")
        print()

