from django.contrib import admin
from .models import Venta

class VentaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    #list_display = ('title', 'author', 'published', 'post_categories')
    #ordering = ('published',)
    #search_fields = ('title', 'author__name', 'categories__name')
    #date_hierarchy = 'published'
    #list_filter = ('categories__name',)

    #Todo esto para mandar llamar las categorias dentro del list_display
    #def post_categories(self, obj):
    #    return "| ".join( [c.name for c in obj.categories.all().order_by("name")] )
    #Esto le cambia el nombre a post_categories
    #post_categories.short_description = 'Tratamiento'

# Esto hace que funcione en el panel de administrador
# Se jala la clase Project del modelo y luego se pasa ProjectAdmin como extendido

admin.site.register(Venta, VentaAdmin)
