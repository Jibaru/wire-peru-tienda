from django.shortcuts import render


def inicio(request):
    return render(request, 'tienda/pages/inicio.html')


def informacion(request):
    return render(request, 'tienda/pages/sobre_nosotros.html')
