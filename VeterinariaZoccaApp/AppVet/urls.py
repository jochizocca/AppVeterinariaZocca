from django.urls import path

from .views import clientes
from .views import turnos
from .views import producto
from .views import animales
from .views import inicio




urlpatterns = [
    path('',inicio,name='Inicio'),
    path('Clientes/', clientes,name='Clientes'),
    path('Turnos/', turnos,name='Turnos'),
    path('Producto/', producto,name='Productos'),
    path('Animales/',animales,name='Animales'),
    
    ]
