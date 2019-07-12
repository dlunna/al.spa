from django.shortcuts import render
from .models import Service

# Create your views here.

def services(request):
    #Esto debuelve todos los objetos que tienen el modelo proyecto
    servicesarray = Service.objects.all()

    # Pasar el parametro en el render como anexo
    # return render(request, "promotion/promotion.html")
    return render(request, "services/services.html", {'servicespaso':servicesarray})
