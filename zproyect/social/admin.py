from django.contrib import admin
from .models import Link

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    #Una vez que estamos manejando usuarios y grupos
    #podemos liminar otros campos para que no los modifique
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('created', 'updated', 'key', 'name')
        else:
            return ('created', 'updated')


admin.site.register(Link, LinkAdmin)