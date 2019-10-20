from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_catalogo),
    path('iniciarSesion/', views.iniciar_sesion),
]
