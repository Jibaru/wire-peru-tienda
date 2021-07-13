from django.shortcuts import render, redirect


def inicio_sesion(request):
    return render(request, 'tienda/pages/inicio_sesion.html')


def iniciar_sesion(request):
    email = request.POST.get('email')
    contrasenia = request.POST.get('contrasenia')
    # TODO: Autenticar y establecer sesion
    return redirect('/')


def registro(request):
    return render(request, 'tienda/pages/registro.html')


def registrar_cliente(request):
    email = request.POST.get('email')
    nombres = request.POST.get('nombres')
    # ...
    # TODO: Registrar cliente
    return redirect('/inicio-sesion')


def cerrar_sesion(request):
    return redirect('/')
