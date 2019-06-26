from django.shortcuts import render
#Para acceder a la BD los modelos importar
from .models import Project

# Create your views here.

def promotion(request):
    #Esto debuelve todos los objetos que tienen el modelo proyecto
    projects = Project.objects.all()
    # Pasar el parametro en el render como anexo
    # return render(request, "promotion/promotion.html")
    return render(request, "promotion/promotion.html", {'projects':projects})
