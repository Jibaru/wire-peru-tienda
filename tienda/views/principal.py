from django.shortcuts import render
from tienda.models import *

def inicio(request):
    articulos= Articulo.objects.all()
    contexto = {
        'articulos': articulos
    }
    return render(request, 'tienda/pages/inicio.html', contexto)


def informacion(request):
    return render(request, 'tienda/pages/sobre_nosotros.html')
