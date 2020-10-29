from django.http import HttpResponse
from django.template.loader import get_template


class HomeView():
    def home(self):
        plantilla = get_template('index.html')
        return HttpResponse(plantilla.render())
    def arduinos(self):
        plantilla = get_template('Arduinos.html')
        return HttpResponse(plantilla.render())
    def sensores(self):
        plantilla = get_template('Sensores.html')
        return HttpResponse(plantilla.render())
    def login(self):
        plantilla = get_template('login.html')
        return HttpResponse(plantilla.render())
    def nosotros(self):
        plantilla = get_template('Nosotros.html')
        return HttpResponse(plantilla.render())
    def contacto(self):
        plantilla = get_template('Contacto.html')
        return HttpResponse(plantilla.render())
    def motores(self):
        plantilla = get_template('Motores.html')
        return HttpResponse(plantilla.render())
    def beaglebone(self):
        plantilla = get_template('Beaglebone.html')
        return HttpResponse(plantilla.render())
    def admin(self):
        plantilla = get_template('Admin.html')
        return HttpResponse(plantilla.render())
    def ingresar_prod(self):
        plantilla = get_template('Ingresar_prod.html')
        return HttpResponse(plantilla.render())
    def listado_prod(self):
        plantilla = get_template('Listado_prod.html')
        return HttpResponse(plantilla.render())