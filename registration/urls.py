from django.urls import path
#from .views import *
from . import views

urlpatterns = [
    #path('login/', views.mostrar_login_v , name='login'),
    #path('login/', views.LoginView.as_view(), name= 'inicio_login'),

    path('RegistrarProveedor/', views.registrar_usuario_proveedor_v, name='registrar_Proveedor'),
    path('RegistrarCliente/', views.registrar_usuario_cliente_v, name='registrar_Cliente'),
]
