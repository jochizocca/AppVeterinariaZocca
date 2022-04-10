from django.http import HttpResponse
from django.shortcuts import render
from .models import Clientes
from .models import Animales
from .models import Turnos
from .models import Productos


def clientes(request):


       
    return render(request,'AppVet/Clientes.html')



def turnos(request):

        
    return render(request,'AppVet/Turnos.html')


def producto(request):

   
    
    return render(request,'AppVet/Productos.html')

def animales(request):

    
    return render(request,'AppVet/Animales.html')

def bienvenida (request):
    return HttpResponse('Bienvenidos a la Veterinaria del Dr Zocca')

def inicio (request):
    return render(request,'AppVet/inicio.html')   