# Generated by Django 4.0.4 on 2022-05-06 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('stock', models.DateField()),
                ('unidad', models.DateField()),
            ],
        ),
    ]
