from django.shortcuts import render


def listar_articulos(request):
    consulta = request.GET.get('consulta') or ''
    # TODO: Realizar busqueda de todos los articulos

    titulo_busqueda = 'Resultados de la búsqueda'
    if not consulta:
        titulo_busqueda = 'Artículos'
    contexto = {
        'titulo_busqueda': titulo_busqueda,
        'consulta': consulta,
        'articulos': []
    }
    return render(request, 'tienda/pages/articulos.html', contexto)


def listar_articulos_por_marca(request, idmarca):
    # TODO: Realizar busqueda de todos los articulos por idmarca
    titulo_busqueda = 'Marca Wacom'
    contexto = {
        'titulo_busqueda': titulo_busqueda,
        'articulos': []
    }
    return render(request, 'tienda/pages/articulos.html', contexto)


def listar_articulos_por_categoria(request, idcategoria):
    # TODO: Realizar busqueda de todos los articulos por idcategoria
    titulo_busqueda = 'Leds'
    contexto = {
        'titulo_busqueda': titulo_busqueda,
        'articulos': []
    }
    return render(request, 'tienda/pages/articulos.html', contexto)


def ver_articulo(request, idarticulo):
    # TODO: Realizar busqueda de articulo por idarticulo
    return render(request, 'tienda/pages/articulo.html')
