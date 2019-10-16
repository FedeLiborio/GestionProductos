from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_catalogo, name='index'),
    path('iniciarSesion', views.iniciar_sesion, name='inicioSesion'),
]
