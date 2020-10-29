"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Views.HomeView import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.home, name="home"),
    path('arduinos/', HomeView.arduinos, name='arduinos'),
    path('sensores/', HomeView.sensores, name='sensores'),
    path('login/', HomeView.login, name='login'),
    path('nosotros', HomeView.nosotros, name='nosotros'),
    path('contacto', HomeView.contacto, name='contacto'),
    path('motores', HomeView.motores, name='motores'),
    path('beaglebone', HomeView.beaglebone, name='beaglebone'),
    path('admin', HomeView.admin, name='admin'),
    path('ingresar_prod', HomeView.ingresar_prod, name='ingresar_prod'),
    path('listado_prod', HomeView.listado_prod, name='listado_prod')
]
