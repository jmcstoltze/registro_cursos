from django.db import models
from django.utils import timezone

# Create your models here.
# Se elige el borrado en cascada sólo para facilitar el desarrollo, pero se sabe que PROTECT es la mejor práctica en un contexto real.

class Profesor(models.Model):
    rut = models.CharField(max_length=9, unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField(default=timezone.now)
    modificacion_registro = models.DateTimeField(default=timezone.now)
    creado_por = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.rut} - {self.apellido}, {self.nombre}"

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["apellido", "nombre"]

class Curso(models.Model):
    codigo = models.CharField(max_length=9, unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    version = models.IntegerField(null=False, blank=False)
    profesores = models.ManyToManyField(Profesor) #################################################

    def __str__(self):
        return f"{self.codigo} - {self.nombre}, {self.version}"

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["codigo", "nombre", "version"]

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField(default=timezone.now)
    modificacion_registro = models.DateTimeField(default=timezone.now)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso) ############################################################

    def __str__(self):
        return f"{self.rut} - {self.apellido}, {self.nombre}"

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ["apellido", "nombre"]

class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    dpto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    region = models.CharField(max_length=50, null=False, blank=False)
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE) #################################################

    def __str__(self):
        return f"{self.calle} - {self.numero}, {self.dpto}, {self.comuna}, {self.region}"

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"
        ordering = ["region", "ciudad", "comuna"]
