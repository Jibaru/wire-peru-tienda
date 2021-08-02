from django.shortcuts import render
from tienda.models import *


def listar_articulos(request):
    consulta = request.GET.get('consulta') or ''
    articulos= Articulo.objects.filter(nombre__icontains=consulta)

    titulo_busqueda = 'Resultados de la búsqueda'
    if not consulta:
        titulo_busqueda = 'Artículos'
    contexto = {
        'titulo_busqueda': titulo_busqueda,
        'consulta': consulta,
        'articulos': articulos
    }
    return render(request, 'tienda/pages/articulos.html', contexto)

 
def listar_articulos_por_marca(request, idmarca):
    articulos=Articulo.objects.filter(id_marca=idmarca)
    titulo_busqueda = Marca.objects.get(id_marca=idmarca).nombre
    contexto = {
        'titulo_busqueda': titulo_busqueda,
        'articulos': articulos
    }
    return render(request, 'tienda/pages/articulos.html', contexto)


def listar_articulos_por_categoria(request, idcategoria):
    articulos=Articulo.objects.filter(articulo_categoria__id_categoria=idcategoria)
    titulo_busqueda = Categoria.objects.get(id_categoria=idcategoria).nombre
    contexto = {
        'titulo_busqueda': titulo_busqueda,
        'articulos': articulos
    }
    return render(request, 'tienda/pages/articulos.html', contexto)


def ver_articulo(request, idarticulo):
    articulo=Articulo.objects.get(id_articulo=idarticulo)
    en_carrito = False
    if 'carrito' in request.session:
        for elemento in request.session['carrito']:
            en_carrito = int(elemento['id_articulo']) == idarticulo

    contexto = {
        'en_carrito': en_carrito,
        'articulo': articulo
    }
    return render(request, 'tienda/pages/articulo.html', contexto)
