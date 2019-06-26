from django.urls import path

# Antes
# from core import views
# No se pueden importar dos veces views, si se tiene que hacer
# usar as XXXXX
from . import views as core_views

urlpatterns = [
    # Mis URLs personales

    #usamos la variable name para los tag URL en html
    path('', core_views.home, name="home"),
    path('acercade/', core_views.about, name="about"),
    #path('servicios/', core_views.services, name="services"),
    path('blog/', core_views.blog, name="blog"),
    path('contacto/', core_views.contact, name="contact"),


    #Codigo para pruebas de backend
    path('ciclos', core_views.ciclos, name="ciclos"),
    path('htmlsimple', core_views.htmlsimple, name="htmlsimple"),
    path('cokie/', core_views.cokie, name="cokie"),
]


