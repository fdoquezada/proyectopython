# Generated by Django 4.0.4 on 2022-05-10 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0008_rename_pedidos_pedido_rename_proveedores_proveedore_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='proveedore',
            name='sub_categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.subcategoria'),
        ),
    ]
