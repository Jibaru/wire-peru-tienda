from django.db import models

# Create your models here.

'''
    Cliente
    Usuario
    Marca
    Categoria
    Pedido
    Articulo
    Articulo_Categoria
    Pedido_Articulo
'''

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    contrasenia = models.CharField(max_length=10, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    dni = models.CharField(max_length=8, blank=False, null=False)
    nombres = models.CharField(max_length=30, blank=False, null=False)
    ap_paterno = models.CharField(max_length=30, blank=False, null=False)
    ap_materno = models.CharField(max_length=30, blank=False, null=False)
    direccion = models.CharField(max_length=40, blank=False, null=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombres']

    def __str__(self):
        return self.nombres

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    estado_pedido = models.CharField(max_length=20, blank=False, null=False)
    num_comprob = models.CharField(max_length=18, blank=False, null=False)
    total = models.FloatField()
    impuesto = models.FloatField()
    serie_comprob = models.CharField(max_length=20, blank=False, null=False)
    tipo_comprob = models.CharField(max_length=40, blank=False, null=False)
    fecha_entrega = models.DateTimeField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['estado_pedido']

    def __str__(self):
        return self.num_comprob

class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    estado_articulo = models.CharField(max_length=20, blank=False, null=False)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    codigo = models.CharField(max_length=20, blank=False, null=False)
    stock = models.IntegerField()
    imagen = models.TextField(blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    precio = models.FloatField()
    id_marca = models.ForeignKey(Marca, on_delete = models.SET_NULL, null = True)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Articulo_Categoria(models.Model):
    id_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, null = True)

class Pedido_Articulo(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete = models.SET_NULL, null = True)
    id_articulo = models.ForeignKey(Articulo, on_delete = models.SET_NULL, null = True)
    cantidad = models.IntegerField()




