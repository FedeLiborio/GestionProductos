from django.shortcuts import render
from GestionProductos.maxproductos.models import *


def mostrar_catalogo(request):
    listaProductos= Producto.objectes.all()
    return render(request, 'maxproductos/mostrarCatalogo.html')
