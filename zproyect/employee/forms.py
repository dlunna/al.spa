from django import forms
from django.utils import timezone
from clients.models import Client
from box.models import Venta

class ClientForm(forms.ModelForm):
    email = forms.EmailField(label="Email",
                             # required=True,
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control', 'placeholder': 'lovely@spa.com'}
                             ),
                             min_length=5,
                             max_length=50)

    birthday = forms.DateTimeField(initial=timezone.localdate(), required=False)

    class Meta:
        model = Client

        fields = ['name', 'fatherlastname', 'motherlastname',
                  'sex', 'email', 'birthday', 'phone', 'work',
                  'facebook', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'fatherlastname': forms.TextInput(attrs={'class':'form-control'}),
            'motherlastname': forms.TextInput(attrs={'class':'form-control'}),
            'sex': forms.TextInput(attrs={'class':'form-control'}),
            #'birthday': forms.DateTimeField(),
            #'email': forms.EmailField(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'work': forms.TextInput(attrs={'class':'form-control'}),
            'facebook': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }

        labels = {
            'name':'Nombre',
            'fatherlastname':'Apellido paterno',
            'motherlastname': 'Apellido materno',
            'sex': 'Genero',
            'birthday': 'Fecha de cumpleaños',
            #'email': 'Dirección de correo electrónico',
            'phone': 'Número celular',
            'work': 'Número de trabajo',
            'facebook': 'Facebook',
            'description': 'Notas adicionales',
        }


class VentaForm(forms.ModelForm):

    class Meta:
        model = Venta

        fields = ['key', 'content', 'cost']

        widgets = {
            'key': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'cost':forms.FloatField()
        }

        labels = {
            'key':'Venta de:',
            'content':'Descripción de la venta',
            'cost': 'Importe',
        }