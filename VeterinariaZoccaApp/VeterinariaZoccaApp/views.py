from datetime import datetime
from django.template import loader
from django.template import Context, Template
from django.http import HttpResponse




def bienvenida (request):
    return HttpResponse('Bienvenidos a la Veterinaria del Dr Zocca')

def inicio (request):

    lista_animales= ["perro","gato","loro"]
    #mihtml = open('C:/Users/Carucha/Desktop/VeterinariaZoccaApp-main/VeterinariaZoccaApp/VeterinariaZoccaApp/Templates/template.html')
    
    #plantilla= Template(mihtml.read())

    #mihtml.close()

    #micontexto = Context({"Hoy": datetime.now(), "mascotas": lista_animales})

    #return HttpResponse(plantilla.render(micontexto))

    plantilla = loader.get_template('template.html')

    return HttpResponse(plantilla.render({"Hoy": datetime.now(), "mascotas": lista_animales}))


