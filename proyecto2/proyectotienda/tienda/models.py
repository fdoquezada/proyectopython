from django.db import models



class Cliente(models.Model):
    rut = models.CharField(max_length=50,unique=True),
    nombre = models.CharField(max_length=50),
    apellidoPaterno = models.CharField(max_length=50),
    apellidoMaterno = models.CharField(max_length=50),
    fecaNacimiento = models.DateField(),
    sexos = [ 
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default=None),
    direccion = models.CharField(max_length=50),
    telefono= models.CharField(max_length=100),
    email= models.EmailField(max_length=100),
    
# Create your models here.

