from django.urls import path

from .views import AgregaClientes, Agregaturno, AnimalesFormulario, ClientesCreate, ClientesDelete, ClientesDetail, ClientesList, ClientesUpdate, ProductosFormulario, TurnosCreate, TurnosDelete, TurnosDetail, TurnosList, TurnosUpdate, buscar, busquedaproductos, editar_perfil, loginView
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
from .views import EditarAnimales
from .views import loginView
from .views import Mensajeclientes
from .views import registrar, editar_perfil
from django.contrib.auth.views import LogoutView
from .views import leerComentarios
from .views import ProductosCreate, ProductosDelete, ProductosDetail,ProductosList,ProductosUpdate



urlpatterns = [
    path('',inicio,name='Inicio'),
    path('Clientes/', clientes,name='Clientes'),
    path('Turnos/', turnos,name='Turnos'),
    path('Producto/', producto,name='Productos'),
    path('Animales/',animales,name='Animales'),
    path('Clientesformulario/',AgregaClientes,name='ClientesFormulario'),
    path('Turnosformulario/',Agregaturno,name='TurnosFormulario'),
    path('Productosformulario/',ProductosFormulario,name='ProductoFormulario'),
    path('Animalesformulario/',AnimalesFormulario,name='AnimalesFormulario'),
    path('busquedaproductos/',busquedaproductos,name='busquedacliente'),
    path('buscar/',buscar,name='buscar'),
    path('busquedaproductos/',busquedaproductos,name='busquedacliente'),
    path('buscar/',buscar,name='buscar'),
    path('leerAnimales/', leerAnimales, name='leerAnimales'),
    path('leerClientes/', leerClientes, name='leerClientes'),
    path('leerProductos/', leerProductos, name='leerProductos'),
    path('leerTurnos/', leerTurnos, name='leerTurnos'),
    path('EliminarAnimales/<id>', EliminarAnimales, name='EliminarAnimales'),
    path('EditarAnimales/<id>', EditarAnimales, name='EditarAnimales'),
    path('clientes/list', ClientesList.as_view(), name='Listclientes'),
    path('clientes/detail/<pk>', ClientesDetail.as_view(), name='Detailclientes'),
    path('clientes/edit/<pk>', ClientesUpdate.as_view(), name='Editclientes'),
    path('clientes/delete/<pk>', ClientesDelete.as_view(), name='Deleteclientes'),
    path('clientes/create/', ClientesCreate.as_view(), name='Newclientes'),   
    path('login/', loginView, name='login'),   
    path('registro/', registrar, name='registrar'),  
    path('logout/', LogoutView.as_view(template_name='AppVet/logout.html'), name='logout'), 
    path('editarperfil/', editar_perfil, name='editar perfil'),
    path('MensajeClientes/',Mensajeclientes,name='MensajeClientes'),
    path('ComentariosLista/',leerComentarios,name='ComentariosLista'),
    path('productos/list/', ProductosList.as_view(), name='List'),
    path('productos/detail/<pk>', ProductosDetail.as_view(), name='Detail'),
    path('productos/edit/<pk>', ProductosUpdate.as_view(), name='Edit'),
    path('productos/delete/<pk>', ProductosDelete.as_view(), name='Delete'),
    path('productos/create/', ProductosCreate.as_view(), name='New'), 
    path('turnos/list/', TurnosList.as_view(), name='Listturnos'),
    path('turnos/detail/<pk>', TurnosDetail.as_view(), name='Detailturnos'),
    path('turnoss/edit/<pk>', TurnosUpdate.as_view(), name='Editturnos'),
    path('turnoss/delete/<pk>', TurnosDelete.as_view(), name='Deleteturnos'),
    path('turnoss/create/', TurnosCreate.as_view(), name='Newturnos'), 
        ] 
        
