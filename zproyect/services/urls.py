from django.urls import path

# Antes
# from core import views
# No se pueden importar dos veces views, si se tiene que hacer
# usar as XXXXX
from . import views as services_views

urlpatterns = [
    # Mis URLs personales

    #usamos la variable name para los tag URL en html
    path('', services_views.services, name="services_home"),
]


