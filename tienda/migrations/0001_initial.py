# Generated by Django 3.2.3 on 2021-07-24 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id_articulo', models.AutoField(primary_key=True, serialize=False)),
                ('estado_articulo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=30)),
                ('codigo', models.CharField(max_length=20)),
                ('stock', models.IntegerField()),
                ('imagen', models.TextField()),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('contrasenia', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('telefono', models.CharField(max_length=10)),
                ('dni', models.CharField(max_length=8)),
                ('nombres', models.CharField(max_length=30)),
                ('ap_paterno', models.CharField(max_length=30)),
                ('ap_materno', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('estado_pedido', models.CharField(max_length=20)),
                ('num_comprob', models.CharField(max_length=18)),
                ('total', models.FloatField()),
                ('impuesto', models.FloatField()),
                ('serie_comprob', models.CharField(max_length=20)),
                ('tipo_comprob', models.CharField(max_length=40)),
                ('fecha_entrega', models.DateTimeField()),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('contrasenia', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido_Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('id_articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.articulo')),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Articulo_Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.articulo')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.categoria')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='id_marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.marca'),
        ),
    ]
