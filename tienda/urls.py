from django.urls import path
from tienda import views

'''
/
/iniciar-sesion
/registro
/carrito
/proceder-compra
/articulos?...
/articulos/{id}
/articulos/categoria/{categoriaid}
/articulos/marca/{marcaid}
'''

urlpatterns = [
    path('', views.inicio),
    path('registro', views.registro),
    path('registrarse', views.registrar_cliente),
    path('inicio-sesion', views.inicio_sesion),
    path('iniciar-sesion', views.iniciar_sesion),
    path('cerrar-sesion', views.cerrar_sesion),
    path('perfil', views.ver_perfil),
    path('actualizar-perfil', views.actualizar_perfil),
    path('articulos', views.listar_articulos),
    path('articulos/<int:idarticulo>', views.ver_articulo),
    path('articulos/categoria/<int:idcategoria>',
         views.listar_articulos_por_categoria),
    path('articulos/marca/<int:idmarca>', views.listar_articulos_por_marca),
    path('carrito', views.carrito),
    path('agregar-articulo', views.agregar_articulo),
    path('remover-articulo', views.remover_articulo),
    path('pedidos', views.listar_pedidos),
    path('verificar-pedido', views.verificar_pedido),
    path('realizar-pedido', views.realizar_pedido),
    path('informacion', views.informacion)
]
