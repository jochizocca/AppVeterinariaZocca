from django.http import HttpResponse
from django.shortcuts import render

from .forms import Animalesformulario, Clientesformulario, Productosformulario, Turnosformulario
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
    if request.method =='POST':
            mi_formulario= Clientesformulario(request.POST)
            
            print(mi_formulario)

            if mi_formulario.is_valid: 
                informacion = mi_formulario.cleaned_data

                nombre=informacion['nombre']
                apellido=informacion['apellido']
                dni=informacion['dni']
                
                clientes= Clientes(nombre=nombre,apellido=apellido,dni=dni)
                clientes.save()
                
                return render(request, "AppVet/Inicio.html")
    else:
            mi_formulario= Clientesformulario()
    return render(request, "AppVet/Clientesformulario.html",{'mi_form': mi_formulario})


def TurnosFormulario (request):
    if request.method =='POST':
            mi_formulario= Turnosformulario(request.POST)
            
            print(mi_formulario)

            if mi_formulario.is_valid: 
                informacion = mi_formulario.cleaned_data

                dia=informacion['dia']
                hora=informacion['hora']
                email=informacion['email']
                
                clientes= Clientes(dia=dia,hora=hora,email=email)
                clientes.save()
                
                return render(request, "AppVet/Inicio.html")
    else:
            mi_formulario= Turnosformulario()
    return render(request, "AppVet/Turnosformulario.html",{'mi_form': mi_formulario})


def AnimalesFormulario (request):
    if request.method =='POST':
            mi_formulario= Animalesformulario(request.POST)
            
            print(mi_formulario)

            if mi_formulario.is_valid: 
                informacion = mi_formulario.cleaned_data

                nombre_animal=informacion['nombre_animal']
                raza=informacion['raza']
                
                
                clientes= Animales(nombre_animal=nombre_animal,raza=raza)
                clientes.save()
                
                return render(request, "AppVet/Inicio.html")
    else:
            mi_formulario= Animalesformulario()
    return render(request, "AppVet/Animalesformulario.html",{'mi_form': mi_formulario})


def ProductosFormulario (request):
    if request.method =='POST':
            mi_formulario= Productosformulario(request.POST)
            
            print(mi_formulario)

            if mi_formulario.is_valid: 
                informacion = mi_formulario.cleaned_data

                n_producto=informacion['n_producto']
                sku=informacion['sku']
                
                
                clientes= Productos(n_producto=n_producto,sku=sku)
                clientes.save()
                
                return render(request, "AppVet/Inicio.html")
    else:
            mi_formulario= Productosformulario()
    return render(request, "AppVet/Productosformulario.html",{'mi_form': mi_formulario})


#def ClientesFormularioPost (request):

    #nombre=request.POST['nombre']
    #apellido=request.POST['apellido']
    #dni=request.POST['dni']

    #mis_clientes= Clientes(nombre=nombre,apellido=apellido,dni=dni)
    #mis_clientes.save()
    
    #return render(request, 'AppVet/Clientes.html', {'nombre':nombre,'apellido':apellido,'dni':dni})

#def AnimalesFormularioPost (request):

    
    #nombre_animal=request.POST['nombre_animal']
    #raza=request.POST['raza']
    

    #mis_animales= Animales(nombre_animal=nombre_animal,raza=raza)
    #mis_animales.save()
    #return render(request, 'AppVet/Animales.html', {'nombre_animal':nombre_animal,'raza':raza})

#def ProductosFormularioPost (request):

    #nombre_producto=request.POST['nombre_producto']
    #sku=request.POST['sku']
    
    #mis_productos= Productos(nombre_producto=nombre_producto,sku=sku)
    #mis_productos.save()
    #return render(request, 'AppVet/Producto.html', {'nombre_producto':nombre_producto,'sku':sku})


#def TurnosFormularioPost (request):

    #dia=request.POST['dia']
    #hora=request.POST['hora']
    #email=request.POST['email']

    #mis_turnos= Turnos(dia=dia,hora=hora,email=email)
    #mis_turnos.save()
    #return render(request, 'AppVet/Turnos.html', {'dia':dia,'hora':hora,'email':email})

def busquedaproductos(request):
    return render(request,'AppVet/busquedaproductos.html')
def buscar(request):
    if request.GET["n_producto"]:
    
        n_producto=request.GET['n_producto']
        sku= Productos.objects.filter(n_producto__icontains=n_producto)

        return render(request, "AppVet/resultadobusqueda.html", {'n_producto':n_producto, 'sku':sku})
    else:
        return HttpResponse ("No enviaste datos")

