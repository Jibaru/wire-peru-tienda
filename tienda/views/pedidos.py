from django.shortcuts import render, redirect


def carrito(request):
    # TODO: cargar datos del carrito
    # los datos estaran guardados en la sesion
    return render(request, 'tienda/pages/carrito.html')


def agregar_articulo(request):
    # TODO: Agregar articulo al carrito
    # FIXME: Debe ser a la misma pagina de donde fue invocado
    return redirect('/')


def verificar_pedido(request):
    # TODO:
    return render(request, 'tienda/pages/verificar_pedido.html')


def realizar_pedido(request):
    # TODO: Realizar pedido
    return render(request, 'tienda/pages/pedido_realizado.html')


def listar_pedidos(request):
    if 'autenticado' not in request.session:
        return redirect('/')
    # TODO: Buscar pedidos
    return render(request, 'tienda/pages/pedidos.html')
