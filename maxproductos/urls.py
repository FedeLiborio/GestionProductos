from django.urls import path
from .views import *

urlpatterns = [
    path('verCarrito/', verCarrito),
    path('procederACheckout/', verCheckout),
     path('verMapa/', verMapa),
     path('agregarProducto/', agregarProducto)
]
