from tienda.models import Cliente
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

def inicio_sesion(request):
    if 'autenticado' in request.session:
        return redirect('/')

    return render(request, 'tienda/pages/inicio_sesion.html')


def iniciar_sesion(request):
    email = request.POST.get('email')
    contrasenia = request.POST.get('contrasenia')

    try:
        cliente = Cliente.objects.get(email = email)
        if not check_password(contrasenia, cliente.contrasenia):
            # Contrasenia incorrecta
            messages.error(request, 'Email o Contraseña incorrecta')
            return render(request, 'tienda/pages/inicio_sesion.html')

        request.session['autenticado'] = True
        request.session['cliente'] = {
            'id_cliente': cliente.id_cliente,
            'nombres': cliente.nombres,
            'ap_paterno': cliente.ap_paterno,
            'ap_materno': cliente.ap_materno,
            'dni': cliente.dni,
            'telefono': cliente.telefono,
            'email': cliente.email,
            'direccion': cliente.direccion
        }
        request.session.modified = True

        return redirect('/')
    except Exception as e:
        print(e)
        messages.error(request, 'Email o Contraseña incorrecta')
        return render(request, 'tienda/pages/inicio_sesion.html')


def registro(request):
    return render(request, 'tienda/pages/registro.html')


def registrar_cliente(request):
    # Datos del formulario
    email = request.POST.get('email')
    nombres = request.POST.get('nombres')
    apepaterno = request.POST.get('apepaterno')
    apematerno = request.POST.get('apematerno')
    contrasenia = request.POST.get('contrasenia')
    
    # Crear cliente
    cliente = Cliente(
        email = email, 
        nombres = nombres, 
        ap_paterno = apepaterno, 
        ap_materno = apematerno, 
        contrasenia = make_password(contrasenia)
    )

    # Registrar cliente
    cliente.save()

    return redirect('/inicio-sesion')


def cerrar_sesion(request):
    del request.session['autenticado']
    del request.session['cliente']
    request.session.modified = True
    return redirect('/')
