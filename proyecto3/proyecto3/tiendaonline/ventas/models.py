from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    telefono=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50, verbose_name="La Direccion")

    def __str__(self): 
        return self.nombre

class Proveedores(models.Model):  
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    mail=models.EmailField(max_length=50)
    telefono=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50, verbose_name="La Direccion")

    def _str_(self):
        return self.nombre

class pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregadr=models.DateField()

    def _str_(self):
        return self.numero

class ventas(models.Model):
    valor=models.IntegerField()
    stock=models.DateField()
    unidad=models.DateField()

    def _str_(self):
        return self.valor

