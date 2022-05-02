from django.contrib import admin

from .models import Avatar, Clientes
from .models import Animales
from .models import Turnos
from .models import Productos

admin.site.register(Clientes)
admin.site.register(Animales)
admin.site.register(Turnos)
admin.site.register(Productos)
admin.site.register(Avatar)

# Register your models here.
