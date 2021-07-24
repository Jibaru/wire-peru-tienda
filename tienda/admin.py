from django.contrib import admin
from .models import *

# Register your models here

admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Pedido)
admin.site.register(Articulo)
admin.site.register(Articulo_Categoria)
admin.site.register(Pedido_Articulo)
