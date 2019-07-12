from django.contrib import admin
from .models import Cuba

# Register your models here.
class CubaAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

admin.site.register(Cuba, CubaAdmin)
