from django.shortcuts import render
from maxproductos.models.Producto import Producto

carrito = []

def vercarrito():
    views.carro.verCarrito(carrito)

def agregarCarrito(producto):
    carrito.append(producto)

def mostrar_catalogo(request):
    list_Producto= Producto.objects.all()
    return render(request, 'maxproductos/mostrar_Catalogo.html',{"objproducto":list_Producto})
