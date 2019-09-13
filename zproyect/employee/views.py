from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from clients.models import Client

# Create your views here.
def employees(request):
    return render(request, 'employee/dashboard.html')

def employeeslist(request):
    pages = get_list_or_404(Client)
    return render(request, 'employee/pages.html', {'pages':pages})

def employeesdetail(request, page_id, page_slug):
    page = get_object_or_404(Client, id=page_id)
    return render(request, 'employee/page.html', {'page':page})

class ClientListView(ListView):
    model = Client
    template_name = 'employee/client_list.html'
    context_object_name = 'pages'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'employee/client_detail.html'
    context_object_name = 'page'

class ClientCreateView(CreateView):
    model = Client
    fields = ['name','fatherlastname','motherlastname']
    template_name = 'employee/client_create.html'
    context_object_name = 'page'

    #def get_success_url(self):
    #    return reverse('empleados')
    success_url = reverse_lazy('empleados')

class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'fatherlastname', 'motherlastname']
    template_name = 'employee/client_update.html'
    #template_name_suffix = '_update'

    def get_success_url(self):
        return reverse_lazy('clientesactualizar', args=[self.object.id]) + '?ok'

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clienteslista')
    template_name = 'employee/client_delete.html'