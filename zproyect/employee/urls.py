# Url de la app empleados
from django.urls import path
#from .views import HomePageView, SamplePageView
from . import views
from .views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView

#urlpatterns = [
#    path('', HomePageView.as_view(), name="home"),
#    path('sample/', SamplePageView.as_view(), name="sample"),
#]

urlpatterns = [
    path('', views.employees, name='empleados'),
    path('clientes/', ClientListView.as_view(), name='clienteslista'),
    path('clientes/<int:pk>/<slug:slug>/', ClientDetailView.as_view(), name='clientesdetalles'),
    path('clientes/nuevo/', ClientCreateView.as_view(), name='clientesnuevo'),
    path('clientes/actualizar/<int:pk>/', views.ClientUpdateView.as_view(), name='clientesactualizar'),
    path('clientes/borrar/<int:pk>/', views.ClientDeleteView.as_view(), name='clientesborrar'),

    #Ejemplos
    path('pages/', views.employeeslist, name='empleadoslist'),
    path('pages/<int:page_id>/<slug:page_slug>/', views.employeesdetail, name='empleadosdetail'),
]
