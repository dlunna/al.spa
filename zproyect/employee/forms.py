from django import forms
from django.utils import timezone
from clients.models import Client
from box.models import Venta

DOY = (
'1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949',
'1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959',
'1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969',
'1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979',
'1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
'1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999',
'2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
'2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
'2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029',
)

class ClientForm(forms.ModelForm):
    email = forms.EmailField(label="Correo electrónico",
                             required=False,
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control', 'placeholder': 'lovely@spa.com'}
                             ),
                             min_length=5,
                             max_length=50)

    #birthday = forms.DateTimeField(initial=timezone.localdate(), required=False)
    birthday = forms.DateField(
        label="Fecha de cumpleaños",
        widget= forms.SelectDateWidget(
            years=DOY
        ),
    )

    class Meta:
        model = Client

        fields = ['name',
                  'fatherlastname',
                  'motherlastname',
                  'sex',
                  'birthday',
                  'email',
                  'celphone',
                  'workplace',
                  'workphone',
                  'facebook',
                  'instagram',
                  'description',
                  ]

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'fatherlastname': forms.TextInput(attrs={'class':'form-control'}),
            'motherlastname': forms.TextInput(attrs={'class':'form-control'}),
            'sex': forms.TextInput(attrs={'class':'form-control'}),
            #'birthday': forms.DateTimeField(),
            #'birthday': forms.SelectDateWidget()),
            #'email': forms.EmailField(attrs={'class':'form-control'}),
            'celphone': forms.TextInput(attrs={'class':'form-control'}),
            'workplace': forms.TextInput(attrs={'class':'form-control'}),
            'workphone': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class':'form-control'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }

        labels = {
            'name':'Nombre',
            'fatherlastname':'Apellido paterno',
            'motherlastname': 'Apellido materno',
            'sex': 'Genero (Hombre - Mujer)',
            #'birthday': 'Fecha de cumpleaños',
            #'email': 'Dirección de correo electrónico',
            'celphone': 'Número celular',
            'workplace': 'Lugar de trabajo',
            'workphone': 'Número de trabajo',
            'facebook': 'Facebook',
            'instagram': 'Instagram!!',
            'description': 'Notas adicionales',
        }


class VentaForm(forms.ModelForm):

    class Meta:
        model = Venta

        fields = ['content', 'cost']

        widgets = {
            #'key': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'cost':forms.FloatField()
        }

        labels = {
            #'key':'Venta de:',
            'content':'Descripción de la venta',
            'cost': 'Importe',
        }