from django.contrib import messages
from django.shortcuts import render, redirect
from tienda.models import Cliente


def ver_perfil(request):
    if 'autenticado' not in request.session:
        return redirect('/')
    return render(request, 'tienda/pages/perfil.html')


def actualizar_perfil(request):
    if 'autenticado' not in request.session:
        return redirect('/')

    id_cliente = request.session['cliente']['id_cliente']
    tipo = request.POST.get('tipo')

    if tipo == 'PERSONAL':
        nombres = request.POST.get('nombres').strip()
        ape_paterno = request.POST.get('apepaterno').strip()
        ape_materno = request.POST.get('apematerno').strip()
        dni = request.POST.get('dni').strip()

        if nombres == '':
            messages.error(request, 'El nombre no puede estar en blanco')
        
        if ape_paterno == '' or ape_materno == '':
            messages.error(request, 'Los apellidos no pueden estar en blanco')
        
        if dni == '':
            messages.error(request, 'El dni no puede estar en blanco')
        
        if len(dni) != 8:
            messages.error(request, 'El dni debe tener 8 caracteres')

        if len(messages.get_messages(request)) > 0:
            return redirect('/perfil')

        cliente = Cliente.objects.get(id_cliente = id_cliente)
        cliente.nombres = nombres
        cliente.ape_paterno = ape_paterno
        cliente.ape_materno = ape_materno
        cliente.dni = dni
        cliente.save()

        request.session['cliente']['nombres'] = nombres
        request.session['cliente']['ape_paterno'] = ape_paterno
        request.session['cliente']['ape_materno'] = ape_materno
        request.session['cliente']['dni'] = dni
        request.session.modified = True

    elif tipo == 'CONTACTO':
        direccion = request.POST.get('direccion').strip()
        telefono = request.POST.get('telefono').strip()
        email = request.POST.get('email').strip()

        if email == '':
            messages.error(request, 'El email no puede estar en blanco')

        if direccion == '':
            messages.error(request, 'La dirección no puede estar en blanco')

        if len(messages.get_messages(request)) > 0:
            return redirect('/perfil')

        cliente = Cliente.objects.get(id_cliente=id_cliente)
        cliente.direccion = direccion
        cliente.email = email
        cliente.telefono = telefono
        cliente.save()

        request.session['cliente']['direccion'] = direccion
        request.session['cliente']['email'] = email
        request.session['cliente']['telefono'] = telefono
        request.session.modified = True

    messages.success(request, 'Actualizado correctamente')

    return redirect('/perfil')
