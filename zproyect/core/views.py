from django.shortcuts import render
from django.shortcuts import HttpResponse

# Variables del sistema
html_base = """
<h1>Proyecto python</h1>
<br/>
<br/>
"""

# Create your views here.
"""
Utilizamos render para mandar llamar los 
templates en HTML dentro de la carpeta
templates/core/
"""

####

def root(request):
    return render(request, "core/root.html")

####

def home(request):
    return render(request, "core/home.html")

def cokie(request):
    return render(request, "core/cokie.html")

def about(request):
    return render(request, "core/about.html")

def services(request):
    return render(request, "core/services.html")

def blog(request):
    return render(request, "core/cokie.html")

def contact(request):
    return render(request, "core/contact.html")


# --------------------------------------------
# Codigo para prueba de backend
# --------------------------------------------

def ciclos(request):
    html_response = "<h1>Inicio</h1>"
    for i in range(10):
        html_response += "<h2>Portada</h2>"
    return HttpResponse(html_response)

"""
HttpResponse genera una respuesta simple de HTML
se le pueden pasar parametros directamente y los 
muestra tal cual en el navegador.
"""
def htmlsimple(request):
    return HttpResponse(html_base + "<h3>Esto es HTML</h3>")