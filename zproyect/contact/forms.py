from django import forms

class ContactForm(forms.Form):
    # en vez de verbose name -> label
    # Requierd para ver si es forzoso o no
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Su nombre'}
    ), min_length=3, max_length=50)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'lovely@spa.com'}
    ), min_length=5, max_length=50)
    phone = forms.CharField(label= "Phone", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'+54 771 lovelyspa'}
    ), min_length=7, max_length=20)
    # En vez de un text fiel se tiene que usar un charfiel
    # para los textos que tienen un texto largo
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control',
               'placeholder':'Deja tu mensaje ...',
               'rows':3}
    ), max_length=150)