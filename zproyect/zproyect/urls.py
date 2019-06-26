"""zproyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from promotion import views as promotion_views
from core import views as core_views
#from services import views as services_views

#Para poder acceder a los archivos multimedia se debe cargar
# el archivo setting en la memoria
from django.conf import settings

urlpatterns = [
    # Importando la APP core
    # ojo con poner la diagonal al final
    path('', core_views.root, name="root"),

    path('spa/', include('core.urls')),

    #usamos la variable name para los tag URL en html
    path('promociones/', promotion_views.promotion, name="promotion"),

    path('servicios/', include('services.urls')),
    #path('servicios/', services_views.services, name="service"),

    # Path del administrador
    path('admin/', admin.site.urls),
]


# una vez se tienen setting en la memoria
# y solo si esta el sistema en modo debug

if settings.DEBUG:
    from django.conf.urls.static import static
    #que ruta va a buscar y cual es la ruta
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


