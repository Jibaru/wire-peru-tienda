import datetime
from functools import reduce
from tienda.models import Articulo
from tienda.models import Cliente
from tienda.models import Pedido
from tienda.models import Pedido_Articulo
from django.shortcuts import render, redirect


def carrito(request):
    total_pagar = 0.0
    if 'pedido' in request.session:
        total_pagar = float(request.session['pedido']['total']) * Pedido.IMPUESTO + Pedido.COSTO_ENVIO

    return render(request, 'tienda/pages/carrito.html', {
        'impuesto': Pedido.IMPUESTO * 100,
        'envio': Pedido.COSTO_ENVIO,
        'tipo_comprobantes': Pedido.TipoComprobante.choices,
        'total_pagar': total_pagar
    })


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
        request.session['pedido']['cantidad_articulos'] = len(request.session['carrito'])

        request.session.modified = True
    except Exception as e:
        print(e)

    return redirect(request.META['HTTP_REFERER'])

def remover_articulo(request):
    if 'carrito' not in request.session:
        return redirect('/carrito')

    id_articulo = request.POST.get('id_articulo')
    i = 0
    encontrado = False
    cantidadElementos = len(request.session['carrito'])
    while not encontrado and i < cantidadElementos:
        encontrado = request.session['carrito'][i]['id_articulo'] == id_articulo
        i += 1

    if encontrado:
        del request.session['carrito'][i - 1]
        total = 0.0
        for articulo in request.session['carrito']:
            total += articulo['subtotal']

        request.session['pedido']['total'] = total
        request.session['pedido']['cantidad_articulos'] = len(request.session['carrito'])

        request.session.modified = True

    return redirect(request.META['HTTP_REFERER'])

def verificar_pedido(request):
    if 'autenticado' not in request.session:
        return redirect('/inicio-sesion')
    if 'carrito' not in request.session:
        return redirect('/')
    if len(request.session['carrito']) == 0:
        return redirect('/')
    total_pagar = 0.0
    if 'pedido' in request.session:
        total_pagar = float(request.session['pedido']['total']) * Pedido.IMPUESTO + Pedido.COSTO_ENVIO

    return render(request, 'tienda/pages/verificar_pedido.html', {
        'impuesto': Pedido.IMPUESTO * 100,
        'envio': Pedido.COSTO_ENVIO,
        'tipo_comprobantes': Pedido.TipoComprobante.choices,
        'total_pagar': total_pagar 
    })


def realizar_pedido(request):
    if 'autenticado' not in request.session:
        return redirect('/inicio-sesion')
    if 'carrito' not in request.session:
        return redirect('/')
    if len(request.session['carrito']) == 0:
        return redirect('/')

    tipo_comprobante = request.POST.get('tipo_comprobante')
    tipo_comprobante = Pedido.TipoComprobante.from_str(tipo_comprobante)

    pedido = Pedido(
        estado_pedido = Pedido.EstadoPedido.PENDIENTE,
        num_comprob = '#',
        total = float(request.session['pedido']['total']) + Pedido.COSTO_ENVIO,
        impuesto = Pedido.IMPUESTO,
        serie_comprob = '#', # Boletas, # FA01 -> Facturas
        tipo_comprob = tipo_comprobante,
        fecha_pedido = datetime.datetime.now(),
        fecha_entrega = datetime.datetime.now() + datetime.timedelta(days=10),
        id_cliente = Cliente.objects.get(id_cliente = request.session['cliente']['id_cliente'])
    )
    pedido.save()
    pedido.num_comprob = F'{pedido.id_cliente}{pedido.id_pedido}'
    
    if tipo_comprobante == Pedido.TipoComprobante.BOLETA:
        pedido.serie_comprob = F'BA{pedido.id_pedido}'
    if tipo_comprobante == Pedido.TipoComprobante.FACTURA:
        pedido.serie_comprob = F'FA{pedido.id_pedido}'
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
