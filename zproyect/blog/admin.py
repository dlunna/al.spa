from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #Se agrega para que en el admin muestre mas columnas
    list_display = ('title', 'author', 'published', 'post_categories')
    #Para ordenamientos
    ordering = ('author', 'published')
    #formulario de busqueda
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    # Para una busqueda por años
    date_hierarchy = 'published'
    # Campos para filtrado
    list_filter = ('author__username', 'categories__name',)

    #Todo esto para mandar llamar las categorias dentro del list_display
    def post_categories(self, obj):
        return "| ".join( [c.name for c in obj.categories.all().order_by("name")] )
    #Esto le cambia el nombre a post_categories
    post_categories.short_description = 'Categorias'

# Esto hace que funcione en el panel de administrador
# Se jala la clase Project del modelo y luego se pasa ProjectAdmin como extendido
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)