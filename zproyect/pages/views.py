from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.

# Se recuperan todas la páginas en un objeto
def pages(request):
    pages = get_object_or_404(Page)
    return render(request, 'pages/avisos.html', {'pages':pages})

#solo se recupera 1 de acuerdo al ID
def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id )
    return render(request, 'pages/aviso.html', {'page':page})