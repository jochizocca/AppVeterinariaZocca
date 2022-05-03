from dataclasses import dataclass
from logging.config import valid_ident
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.decorators import login_required 

from .forms import Animalesformulario, Clientesformulario, Productosformulario, Turnosformulario, UserEditForm
from .forms import MensajeClientes
from .models import Avatar, Clientes
from .models import Animales
from .models import Turnos
from .models import Productos

@login_required
def clientes(request):


       
    return render(request,'AppVet/Clientes.html')


@login_required
def turnos(request):

        
    return render(request,'AppVet/Turnos.html')


def producto(request):

   
    
    return render(request,'AppVet/Productos.html')
@login_required
def animales(request):

    
    return render(request,'AppVet/Animales.html')

def bienvenida (request):
    return HttpResponse('Bienvenidos a la Veterinaria del Dr Zocca')

def inicio (request):
    avatar=Avatar.objects.get(user=request.user.id)
    return render(request,'AppVet/inicio.html', {'avatar':avatar})   

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

def inicio (request):
    avatar=Avatar.objects.get(user=request.user.id)
    return render(request,'AppVet/inicio.html', {'avatar':avatar})   

@login_required
def Mensajeclientes (request):
    if request.method =='POST':
            mi_formulario= MensajeClientes(request.POST)
            
            print(mi_formulario)

            if mi_formulario.is_valid: 
                informacion = mi_formulario.cleaned_data

                nombre=informacion['nombre']
                apellido=informacion['apellido']
                comentarios=informacion['comentarios']
                
                mensajeclientes= MensajeClientes(nombre=nombre,apellido=apellido,comentarios=comentarios)
                mensajeclientes.save()
                
                return render(request, "AppVet/Inicio.html")
    else:
            mi_formulario= MensajeClientes()
    return render(request, "AppVet/MensajeClientes.html",{'mi_form': mi_formulario})


def TurnosFormulario (request):
    if request.method =='POST':
            mi_formulario= Turnosformulario(request.POST)
            
            print(mi_formulario)

            if mi_formulario.is_valid: 
                informacion = mi_formulario.cleaned_data

                dia=informacion['dia']
                hora=informacion['hora']
                email=informacion['email']
                
                turnos= Turnos(dia=dia,hora=hora,email=email)
                turnos.save()
                
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
                
                
                animales= Animales(nombre_animal=nombre_animal,raza=raza)
                animales.save()
                
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
                
                
                productos= Productos(n_producto=n_producto,sku=sku)
                productos.save()
                
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


def leerAnimales(request):
    animales = Animales.objects.all()
    
    contexto= {"lista_animales": animales} 
    return  render (request , 'AppVet/leerAnimales.html', contexto)

def leerClientes(request):
    clientes = Clientes.objects.all()
    
    contexto= {"lista_clientes": clientes} 
    return  render (request , 'AppVet/leerClientes.html', contexto)

def leerProductos(request):
    productos = Productos.objects.all()
    
    contexto= {"lista_productos": productos} 
    return  render (request , 'AppVet/leerProductos.html', contexto)

def leerTurnos(request):
    turnos = Turnos.objects.all()
    
    contexto= {"lista_turnos": turnos} 
    return  render (request , 'AppVet/leerTurnos.html', contexto)

def EliminarAnimales(request, id):
    animales = Animales.objects.get(id=id)
    animales.delete()
    
    animales = Animales.objects.all()
    
    contexto= {"lista_animales": animales} 
    return  render (request , 'AppVet/leerAnimales.html', contexto)

def EditarAnimales(request,id):
    animales = Animales.objects.get(id=id)
    
    if request.method== 'POST':

        mi_formulario= Animalesformulario(request.POST)
        

        if mi_formulario.is_valid():
            informacion= mi_formulario.cleaned_data

            Animales.nombre_animal= informacion['nombre']
            Animales.raza= informacion['raza']

            Animales.save()

            return render(request, 'AppVet/inicio.html')

    else:

        mi_formulario = Animalesformulario(
           initial={
               'nombre_animal': animales.nombre_animal,
               'raza': animales.raza
           }
        )

    return render(request, 'AppVet/EditarAnimales.html', {"mi_formulario":mi_formulario})

class ClientesList(ListView):
    model= Clientes
    template_name= "AppVet/clientes_list.html"

class ClientesDetail(DetailView):
    model= Clientes
    template_name= "AppVet/clientes_detalle.html"

class ClientesCreate(LoginRequiredMixin,CreateView):
    model=Clientes
    succes_url= 'AppVet/Clientes/list'
    fields=['nombre','apellido','dni']

class ClientesUpdate(LoginRequiredMixin,UpdateView):
    model=Clientes
    succes_url= 'AppVet/Clientes/list'
    fields=['nombre','apellido','dni']

class ClientesDelete(LoginRequiredMixin,DeleteView):
    model=Clientes
    template_name= "AppVet/clientes_delete.html"
    succes_url= 'AppVet/Clientes/list'

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            usuario= datos ['username']
            psw = datos ['password']

            user = authenticate(username=usuario, password=psw)

            if user:
                login(request,user)
                return render(request,"AppVet/inicio.html",{"mensaje": f'Bienvenido {usuario}'})


            else:

                return render(request,"AppVet/inicio.html",{"mensaje": 'Datos Incorrectos'})
    
    else:
        form=AuthenticationForm()
    return render(request, "AppVet/login.html", {'form': form})


def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm( request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']

            form.save()
            return render(request, "AppVet/inicio.html",{'mensaje': f'Usuario creado con exito: {username}'})           
 
    else:
        form=UserCreationForm()
    return render(request, "AppVet/registrar.html", {'form': form})

@login_required
def editar_perfil(request):
    usuario=request.user
    if request.method=='POST':
       
        mi_formulario= UserEditForm(request.POST)
        
        if mi_formulario.is_valid():
         
          data=mi_formulario.cleaned_data

          usuario.email=data['email'] 
          usuario.password1=data['password1'] 
          usuario.password2=data['password2'] 
          usuario.first_name=data['first_name']
          usuario.last_name=data['last_name']
          usuario.save()

          return render(request,'AppVet/inicio.html')

    else:

        mi_formulario=UserEditForm(initial={'email':usuario.email})

    return render(request, "AppVet/editarperfil.html",{"mi_formulario":mi_formulario})

