# Generated by Django 4.0.4 on 2022-05-06 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_ventas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='La Direccion'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='La Direccion'),
        ),
    ]