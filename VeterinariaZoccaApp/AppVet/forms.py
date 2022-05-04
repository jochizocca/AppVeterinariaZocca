from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Clientesformulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    dni=forms.IntegerField()
    link=forms.IntegerField()
    animales=forms.IntegerField()

class Animalesformulario(forms.Form):
    nombre_animal= forms.CharField()
    raza= forms.CharField()
    

class Turnosformulario(forms.Form):
    dia= forms.DateField(widget = forms.SelectDateWidget)
    hora= forms.CharField()
    email=forms.EmailField()

class Productosformulario(forms.Form):
    n_producto= forms.CharField()
    sku=forms.IntegerField()

class MensajeClientes(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    comentarios= forms.CharField()

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label='Modificar email')
    password1= forms.CharField(label='Contrasena', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir Contrasena ', widget=forms.PasswordInput)
    firts_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')



class Meta:
    model= User 
    fields=['email','first_name','last_name','password1','password2']
    help_text={k:"" for k in fields}



