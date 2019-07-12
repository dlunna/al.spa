from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Cuba
#Para las vistas en clases
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
class cubaListView(ListView):
    model = Cuba

class cubaDetailView(DetailView):
    model = Cuba

class cubaCreateView(CreateView):
    model = Cuba
    fields = ['title','content']
