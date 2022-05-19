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
    nombre=models.CharField(max_length=50, verbose_name="nombre subcategoria")

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="nombre categoria")

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)
    subcategoria=models.ForeignKey(Subcategoria, null=True, on_delete=models.CASCADE) 
    correo=models.EmailField(max_length=100)
    ciudad=models.CharField(max_length=50)
    telefono=models.CharField(max_length=15)

    def __str__(self):
        return self .nombre



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
    
opciones_consulta = [
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugenecia"],
    [3,"Felicitaciones"]
]
    


class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    tipo_consulta =models.IntegerField(choices=opciones_consulta)
    mensaje= models.TextField()
    avisos =models.BooleanField()
    
    def __str__(self):
        return self.nombre
    

