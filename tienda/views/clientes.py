from django.shortcuts import render, redirect


def ver_perfil(request):
    # TODO: Cargar perfil del usuario sesion
    return render(request, 'tienda/pages/perfil.html')


def actualizar_perfil(request):
    # TODO: Actualizar perfil del usuario sesion
    return redirect('/perfil')
