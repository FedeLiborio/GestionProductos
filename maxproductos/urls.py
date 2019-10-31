from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_catalogo_v, name='/'),
    path('iniciarSesion/', views.iniciar_sesion_v, name='iniciar_Sesion'),
    path('registrarUsuario/', views.registrar_usuario_v, name='registrar_Usuario'),
    path('detalleProducto/<int:idProducto>/', views.detalle_producto_v, name='detalle_Producto'),
    path('verCarrito/', views.verCarrito, name='ver_Carrito'),
    path('procederACheckout/', views.verCheckout),
    path('verMapa/', views.verMapa),

    # parece ser que debe terminar el nombre(no name) de la url con / para que
    # funcione el {% url %} en el template

    # el nombre de la variable del parametro del path tiene que ser igual al parametro del la funcion 
    # de la vista


]
