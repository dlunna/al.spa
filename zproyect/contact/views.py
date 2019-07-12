from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.

def contact(request):
    print("Tipo de petición ---> {}".format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            content = request.POST.get('content', '')
            # Suponemos que todo va bien, redireccionar
            # lo de abajo es con la url estatica
            #return redirect('/contact/?ok')
            #con la funcion reversa; agregar la libreria
            # y enviamos el correo

            email =EmailMessage(
                "Lovely Spa: nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["dlunna@gmail.com"],
                reply_to=[email],

            )
            try:
                email.send()
                print("--> Se envio correctamente <--")
                return redirect(reverse('contact') + "?ok")
            except:
                print("Algo no ha ido bien")
                return redirect(reverse('contact') + "?fail")

            #return redirect(reverse('contact')+"?ok")

    return render(request, "contact/contact.html", {'form':contact_form})
