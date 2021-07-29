import datetime
from functools import reduce
from tienda.models import Articulo
from tienda.models import Cliente
from tienda.models import Pedido
from tienda.models import Pedido_Articulo
from django.shortcuts import render, redirect


def carrito(request):
    return render(request, 'tienda/pages/carrito.html')


def agregar_articulo(request):
    id_articulo = request.POST.get('id_articulo')
    cantidad = int(request.POST.get('cantidad'))

    try:
        articulo = Articulo.objects.get(id_articulo = id_articulo)
        if 'carrito' not in request.session:
            request.session['carrito'] = []
        if 'pedido' not in request.session:
            request.session['pedido'] = {}
        
        request.session['carrito'].append({
            'id_articulo': id_articulo,
            'nombre': articulo.nombre,
            'imagen': articulo.imagen,
            'descripcion': articulo.descripcion,
            'stock': articulo.stock,
            'precio': articulo.precio,
            'cantidad': cantidad,
            'subtotal': articulo.precio * cantidad,
            'pagina': F'/articulos/{articulo.id_articulo}'
        })

        total = 0.0
        for articulo in request.session['carrito']:
            total += articulo['subtotal']

        request.session['pedido']['total'] = total
        request.session['pedido']['envio'] = 10.0
        request.session['pedido']['cantidad_articulos'] = len(request.session['carrito'])

        request.session.modified = True
    except Exception as e:
        print(e)

    return redirect("/")


def verificar_pedido(request):
    if 'autenticado' not in request.session:
        return redirect('/inicio-sesion')
    if 'carrito' not in request.session:
        return redirect('/')
    if len(request.session['carrito']) == 0:
        return redirect('/')

    return render(request, 'tienda/pages/verificar_pedido.html')


def realizar_pedido(request):
    if 'autenticado' not in request.session:
        return redirect('/inicio-sesion')
    if 'carrito' not in request.session:
        return redirect('/')
    if len(request.session['carrito']) == 0:
        return redirect('/')
    pedido = Pedido(
        estado_pedido = 'PENDIENTE',
        num_comprob = '0123ABC',
        total = request.session['pedido']['total'],
        impuesto = request.session['pedido']['envio'],
        serie_comprob = '1BC',
        tipo_comprob = 'BOLETA',
        fecha_pedido = datetime.datetime.now(),
        fecha_entrega = datetime.datetime.now(),
        id_cliente = Cliente.objects.get(id_cliente = request.session['cliente']['id_cliente'])
    )
    pedido.save()

    for articulo in request.session['carrito']:
        pedido_articulo = Pedido_Articulo(
            id_pedido = Pedido.objects.get(id_pedido = pedido.id_pedido),
            id_articulo = Articulo.objects.get(id_articulo = articulo['id_articulo']),
            cantidad = articulo['cantidad']
        )
        pedido_articulo.save()

    del request.session['carrito']
    del request.session['pedido']
    request.session.modified = True

    return render(request, 'tienda/pages/pedido_realizado.html', { pedido: pedido })


def listar_pedidos(request):
    if 'autenticado' not in request.session:
        return redirect('/')
    id_cliente = request.session['cliente']['id_cliente']
    pedidos = Pedido.objects.filter(id_cliente = id_cliente)
    return render(request, 'tienda/pages/pedidos.html', { 'pedidos': pedidos })
