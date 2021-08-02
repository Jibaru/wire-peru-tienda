# Generated by Django 3.2.5 on 2021-08-02 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_auto_20210801_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='estado_articulo',
            field=models.CharField(choices=[('HABILITADO', 'Habilitado'), ('DESHABILITADO', 'Deshabilitado')], default='HABILITADO', max_length=20),
        ),
        migrations.AlterField(
            model_name='articulo_categoria',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado_pedido',
            field=models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('COMPLETADO', 'Completado'), ('CANCELADO', 'Cancelado')], default='PENDIENTE', max_length=20),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tipo_comprob',
            field=models.CharField(choices=[('BOLETA', 'Boleta'), ('FACTURA', 'Factura')], default='BOLETA', max_length=40),
        ),
        migrations.AlterField(
            model_name='pedido_articulo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
