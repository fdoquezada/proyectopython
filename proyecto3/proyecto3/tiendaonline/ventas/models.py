from re import sub
from django.db import models
from django.urls import reverse

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    telefono=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)

    def __str__(self): 
        return self.nombre
        
class Subcategoria(models.Model):
   sub_categoria=models.CharField(max_length=50)

   def __str__(self):
       return self.sub_categoria



class Categoria(models.Model):
    nombre_categoria=models.CharField(max_length=50)
    sub_categoria=models.ForeignKey(Subcategoria, null=True, on_delete=models.SET_NULL)


    def __str__(self): 
        return self.nombre_categoria

    
class Proveedore(models.Model):  
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    mail=models.EmailField(max_length=50)
    telefono=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    categoria=models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre

class pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregadr=models.DateField()

    def _str_(self):
        return self.numero

class venta(models.Model):
    valor=models.IntegerField()
    stock=models.DateField()
    unidad=models.DateField()

    def _str_(self):
        return self.valor


