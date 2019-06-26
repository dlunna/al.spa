from django.contrib import admin
#importa el modelo la BD y le dice que va a usar
#la clase Project
from .models import Project

# Register your models here.
# Esto hace que funcione en el panel de administrador
admin.site.register(Project)