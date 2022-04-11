from django.urls import path

from .views import AnimalesFormulario, AnimalesFormularioPost, ClientesFormulario, ClientesFormularioPost, ProductosFormulario, ProductosFormularioPost, TurnosFormulario, clientes
from .views import turnos
from .views import producto
from .views import animales
from .views import inicio
from .views import TurnosFormularioPost




urlpatterns = [
    path('',inicio,name='Inicio'),
    path('Clientes/', clientes,name='Clientes'),
    path('Turnos/', turnos,name='Turnos'),
    path('Producto/', producto,name='Productos'),
    path('Animales/',animales,name='Animales'),
    path('Clientesformulario/',ClientesFormulario,name='ClientesFormulario'),
    path('Turnosformulario/',TurnosFormulario,name='TurnosFormulario'),
    path('Productoformulario/',ProductosFormulario,name='ProductoFormulario'),
    path('Animalesformulario/',AnimalesFormulario,name='AnimalesFormulario'),
    path('ClientesformularioPost/',ClientesFormularioPost,name='ClientesFormularioPost'),
    path('TurnosformularioPost/',TurnosFormularioPost,name='TurnossFormularioPost'),
    path('ProductoformularioPost/',ProductosFormularioPost,name='ProductoFormularioPost'),
    path('AnimalesformularioPost/',AnimalesFormularioPost,name='AnimalesFormularioPost')
    ]
