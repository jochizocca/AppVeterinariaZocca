from django.urls import path

from .views import AnimalesFormulario, ClientesFormulario, ProductosFormulario, TurnosFormulario, buscar, busquedaproductos
from .views import turnos
from .views import clientes
from .views import producto
from .views import animales
from .views import inicio
from .views import leerAnimales
from .views import leerClientes
from .views import leerProductos
from .views import leerTurnos
from .views import EliminarAnimales






urlpatterns = [
    path('',inicio,name='Inicio'),
    path('Clientes/', clientes,name='Clientes'),
    path('Turnos/', turnos,name='Turnos'),
    path('Producto/', producto,name='Productos'),
    path('Animales/',animales,name='Animales'),
    path('Clientesformulario/',ClientesFormulario,name='ClientesFormulario'),
    path('Turnosformulario/',TurnosFormulario,name='TurnosFormulario'),
    path('Productosformulario/',ProductosFormulario,name='ProductoFormulario'),
    path('Animalesformulario/',AnimalesFormulario,name='AnimalesFormulario'),
    #path('ClientesformularioPost/',ClientesFormularioPost,name='ClientesFormularioPost'),
    #path('TurnosformularioPost/',TurnosFormularioPost,name='TurnossFormularioPost'),
    #path('ProductoformularioPost/',ProductosFormularioPost,name='ProductoFormularioPost'),
    #path('AnimalesformularioPost/',AnimalesFormularioPost,name='AnimalesFormularioPost'),
    path('busquedaproductos/',busquedaproductos,name='busquedacliente'),
    path('buscar/',buscar,name='buscar'),
     path('busquedaproductos/',busquedaproductos,name='busquedacliente'),
    path('buscar/',buscar,name='buscar'),
    path('leerAnimales/', leerAnimales, name='leerAnimales'),
    path('leerClientes/', leerClientes, name='leerClientes'),
    path('leerProductos/', leerProductos, name='leerProductos'),
    path('leerTurnos/', leerTurnos, name='leerTurnos'),
    path('EliminarAnimales/<id>', EliminarAnimales, name='EliminarAnimales'),


        ]
