# Generated by Django 4.0.4 on 2022-05-23 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='STOCK',
            new_name='stock',
        ),
    ]