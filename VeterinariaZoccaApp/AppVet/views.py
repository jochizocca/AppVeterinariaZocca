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

def ClientesFormulario (request):
    return render(request, "AppVet/Clientesformulario.html")

def TurnosFormulario (request):
    return render(request, "AppVet/Turnosformulario.html")

def AnimalesFormulario (request):
    return render(request, "AppVet/Animalesformulario.html")

def ProductosFormulario (request):
    return render(request, "AppVet/Productosformulario.html")

def ClientesFormularioPost (request):

    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    dni=request.POST['dni']

    mis_clientes= Clientes(nombre=nombre,apellido=apellido,dni=dni)
    mis_clientes.save()
    return render(request, 'AppVet/Clientes.html', {'nombre':nombre,'apellido':apellido,'dni':dni})

def AnimalesFormularioPost (request):

    nombre_animal=request.POST['nombre_animal']
    raza=request.POST['raza']
    

    mis_animales= Animales(nombre_animal=nombre_animal,raza=raza)
    mis_animales.save()
    return render(request, 'AppVet/Animales.html', {'nombre_animal':nombre_animal,'raza':raza})

def ProductosFormularioPost (request):

    nombre_producto=request.POST['nombre_producto']
    sku=request.POST['sku']
    
    mis_productos= Productos(nombre_producto=nombre_producto,sku=sku)
    mis_productos.save()
    return render(request, 'AppVet/Producto.html', {'nombre_producto':nombre_producto,'sku':sku})


def TurnosFormularioPost (request):

    dia=request.POST['dia']
    hora=request.POST['hora']
    email=request.POST['email']

    mis_turnos= Turnos(dia=dia,hora=hora,email=email)
    mis_turnos.save()
    return render(request, 'AppVet/Turnos.html', {'dia':dia,'hora':hora,'email':email})



