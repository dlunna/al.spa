# Es para extender el diccionario de contexto
# Digamos como variables globales
# se tiene que habilitar en:
# settings -> templates -> context_processors

from .models import Link

#def ctx_dict(request):
#    ctx = {'test':'hola'}
#    return ctx

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url

    return ctx
