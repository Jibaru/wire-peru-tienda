from django.shortcuts import render
from tienda.models import *


def listar_articulos(request):
    consulta = request.GET.get('consulta') or ''
    # ODOT: Realizar busqueda de todos los articulos
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

    ''' 

    idmarca=Marca.objects.filter('id_marca')
    # ODO:T Realizar busqueda de todos los articulos por idmarca
    articulos= request.articulo.marca_set.filter(idmarca)'''

    articulos=Articulo.objects.filter(id_marca=idmarca)
    titulo_busqueda = Marca.objects.get(id_marca=idmarca).nombre
    contexto = {
        'titulo_busqueda': titulo_busqueda,
        'articulos': articulos
    }
    return render(request, 'tienda/pages/articulos.html', contexto)


def listar_articulos_por_categoria(request, idcategoria):
    
    # :DOTO Realizar busqueda de todos los articulos por idcategoria
    articulos=Articulo.objects.filter(articulo_categoria__id_categoria=idcategoria)
    titulo_busqueda = Categoria.objects.get(id_categoria=idcategoria).nombre
    contexto = {
        'titulo_busqueda': titulo_busqueda,
        'articulos': articulos
    }
    return render(request, 'tienda/pages/articulos.html', contexto)


def ver_articulo(request, idarticulo):
    # DO: Realizar busqueda de articulo por idarticulo 
    articulo=Articulo.objects.get(id_articulo=idarticulo)
    #marca = Marca.objects.get(id_marca=articulo.id_marca.nombre).nombre

    contexto = {
        #'marca':marca,
        
        'articulo': articulo
    }
    return render(request, 'tienda/pages/articulo.html', contexto)
















'''
def listar_articulos(request):
    consulta = request.GET.get('consulta') or ''
    # ODOT: Realizar busqueda de todos los articulos

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
    # ODO:T Realizar busqueda de todos los articulos por idmarca
    titulo_busqueda = 'Marca Wacom'
    contexto = {
        'titulo_busqueda': titulo_busqueda,
        'articulos': []
    }
    return render(request, 'tienda/pages/articulos.html', contexto)


def listar_articulos_por_categoria(request, idcategoria):
    # :DOTO Realizar busqueda de todos los articulos por idcategoria
    titulo_busqueda = 'Leds'
    contexto = {
        'titulo_busqueda': titulo_busqueda,
        'articulos': []
    }
    return render(request, 'tienda/pages/articulos.html', contexto)


def ver_articulo(request, idarticulo):
    # DO: Realizar busqueda de articulo por idarticulo 
    return render(request, 'tienda/pages/articulo.html')
'''