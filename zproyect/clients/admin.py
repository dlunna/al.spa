from django.contrib import admin
from .models import Client

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    # Esta clase media es para darle responsive al ckeditor
    class Media:
        css = {
            'all': ('employee/css/custom_ckeditor.css',)
        }

admin.site.register(Client, ClientAdmin)