# Generated by Django 4.0.4 on 2022-05-03 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidoPaterno', models.CharField(max_length=50)),
                ('apellidoMaterno', models.CharField(max_length=50)),
                ('fecaNacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
