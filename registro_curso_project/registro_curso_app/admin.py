from django.contrib import admin
from .models import Profesor, Curso, Estudiante, Direccion

# Register your models here.

admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Direccion)
