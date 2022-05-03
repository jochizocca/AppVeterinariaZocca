from django.contrib import admin

from .models import Avatar, Clientes
from .models import Animales
from .models import Turnos
from .models import Productos

class ClientesAdmin(admin.ModelAdmin):
    list_display=['nombre','apellido','dni']
    search_fields=['nombre','apellido']

admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Animales)
admin.site.register(Turnos)
admin.site.register(Productos)
admin.site.register(Avatar)

# Register your models here.
