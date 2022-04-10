from django.db import models



# Create your models here.

class Clientes(models.Model):
    nombre= models.CharField('nombre',max_length=20) 
    apellido=models.CharField('apellido',max_length=20) 
    dni=models.IntegerField('dni')
    
       
class Turnos(models.Model):
    dia=models.CharField('dia',max_length=20)
    hora=models.CharField('hora',max_length=20)
    email=models.EmailField()

class Productos(models.Model):
    n_producto= models.CharField('n_producto',max_length=20)
    sku=models.IntegerField()

class Animales(models.Model):
    nombre_animal= models.CharField('nombre_animal',max_length=20)
    raza=models.CharField('raza',max_length=20)



