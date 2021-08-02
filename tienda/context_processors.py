from tienda.models import Categoria, Marca

def categorias_marcas(request):
    return {
        'categorias_nav': Categoria.objects.all(),
        'marcas_nav': Marca.objects.all()
    }