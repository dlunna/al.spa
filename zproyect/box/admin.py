from django.contrib import admin
from .models import Venta

class VentaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    list_display = ('content', 'cost', 'client', 'salesmen', 'salesdate')
    #ordering = ('cost',)
    #search_fields = ('client', 'salesmen')
    #date_hierarchy = 'published'
    list_filter = ('client__name',)
    #list_filter = ('author__username', 'categories__name',)

    #Todo esto para mandar llamar las categorias dentro del list_display
    #def post_categories(self, obj):
    #    return "| ".join( [c.name for c in obj.categories.all().order_by("name")] )
    #Esto le cambia el nombre a post_categories
    #post_categories.short_description = 'Tratamiento'

# Esto hace que funcione en el panel de administrador
# Se jala la clase Project del modelo y luego se pasa ProjectAdmin como extendido

admin.site.register(Venta, VentaAdmin)
