from django.db import models
from django.contrib.auth.models import User
from django.forms import DateField, DateTimeField


# Create your models here.

class Clientes(models.Model):
    nombre= models.CharField('nombre',max_length=20) 
    apellido=models.CharField('apellido',max_length=20) 
    dni=models.IntegerField('dni')
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'
    
       
class Turnos(models.Model):
    dia=models.DateField()
    hora=models.DateTimeField()
    email=models.EmailField()
    link=models.CharField(max_length=20)
    cliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
   

    
   
    def __str__(self) -> str:
        return f'{self.dia} {self.hora}'


class Productos(models.Model):
    n_producto= models.CharField('n_producto',max_length=20)
    sku=models.IntegerField()

    def __str__(self) -> str:
        return f'{self.n_producto}'

class Animales(models.Model):
    nombre_animal= models.CharField('nombre_animal',max_length=20)
    raza=models.CharField('raza',max_length=20)
    link=models.CharField(max_length=20)
    cliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
  

    def __str__(self) -> str:
        return f'{self.nombre_animal} {self.raza}'



class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares',null=True)