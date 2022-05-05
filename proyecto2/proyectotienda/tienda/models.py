from tokenize import Comment
from django.db import models



class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellidoPaterno=models.CharField(max_length=50)
    apellidoMaterno=models.CharField(max_length=50)
    fecaNacimiento=models.DateField()
    direccion=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    telefono=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

    def _str_(self):
        return self.nombre + " " + self.apellidoPaterno + " " + self.apellidoMaterno
        
class Proveedores(models.Model):
    nombre=models.CharField(max_length=50)
    apellidoPaterno=models.CharField(max_length=50)
    apellidoMaterno=models.CharField(max_length=50)
    fecaNacimiento=models.DateField()
    direccion=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    telefono=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)    

    def _str_(self):
        return self.nombre + " " + self.apellidoPaterno + " " + self.apellidoMaterno


# Create your models here.

