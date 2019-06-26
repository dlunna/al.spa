from django.contrib import admin
from .models import Project

# Register your models here.

# Una clase para extender las funcionalidades del panel de admin
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Esto hace que funcione en el panel de administrador
# Se jala la clase Project del modelo y luego se pasa ProjectAdmin como extendido
admin.site.register(Project, ProjectAdmin)