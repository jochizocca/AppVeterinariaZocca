from django import forms

class Clientesformulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    dni=forms.IntegerField()

class Animalesformulario(forms.Form):
    nombre_animal= forms.CharField()
    raza= forms.CharField()
    

class Turnosformulario(forms.Form):
    dia= forms.CharField()
    hora= forms.CharField()
    email=forms.EmailField()

class Productosformulario(forms.Form):
    n_producto= forms.CharField()
    sku=forms.IntegerField()
