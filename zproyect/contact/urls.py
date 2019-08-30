from django.urls import path
from . import views as core_views

urlpatterns = [
    # Mis URLs personales
    path('', core_views.contact, name="contact"),
    path('emailcontact/', core_views.emailcontact, name="emailcontact"),
]


