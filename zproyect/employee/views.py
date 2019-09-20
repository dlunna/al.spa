from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from clients.models import Client
from box.models import Venta
from .forms import ClientForm

class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario sea
    miembro del staff
    """

    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class StaffRequiredDecorator(object):
    """
    Este decorador de metodo para no usar mixin
    y quitar el if
    necesita:
    from django.contrib.admin.views.decorators import staff_member_required
    from django.utils.decorators import method_decorator
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredDecorator, self).dispatch(request, *args, **kwargs)


# Create your views here.
def employees(request):
    return render(request, 'employee/dashboard.html')

def employeeslist(request):
    pages = get_list_or_404(Client)
    return render(request, 'employee/pages.html', {'pages':pages})

def employeesdetail(request, page_id, page_slug):
    page = get_object_or_404(Client, id=page_id)
    return render(request, 'employee/page.html', {'page':page})




class ClientListView(StaffRequiredMixin, ListView):
    model = Client
    template_name = 'employee/client_list.html'
    context_object_name = 'pages'

@method_decorator(staff_member_required, name='dispatch')
class ClientDetailView(DetailView):
    model = Client
    template_name = 'employee/client_detail.html'
    context_object_name = 'page'

class ClientCreateView(StaffRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'employee/client_create.html'
    context_object_name = 'page'
    #def get_success_url(self):
    #    return reverse('empleados')
    success_url = reverse_lazy('empleados')

class ClientUpdateView(StaffRequiredMixin, UpdateView):
    model = Client
    fields = ['name', 'fatherlastname', 'motherlastname']
    template_name = 'employee/client_update.html'
    #template_name_suffix = '_update'

    def get_success_url(self):
        return reverse_lazy('clientesactualizar', args=[self.object.id]) + '?ok'

class ClientDeleteView(StaffRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clienteslista')
    template_name = 'employee/client_delete.html'




################################
# Ventas de la caja
################################

@method_decorator(staff_member_required, name='dispatch')
class VentaListView(ListView):
    model = Venta
    template_name = 'employee/box_list.html'
    context_object_name = 'pages'

#@method_decorator(staff_member_required, name='dispatch')
#class VentaCreateView(CreateView):
#    model = Venta
#    template_name = 'employee/box_create.html'
#    context_object_name = 'page'

@method_decorator(staff_member_required, name='dispatch')
class VentaCreateView(CreateView):
    model = Venta
    fields = ['key', 'content', 'cost', 'salesmen','client']
    template_name = 'employee/box_create.html'
    context_object_name = 'page'
    success_url = reverse_lazy('empleados')
