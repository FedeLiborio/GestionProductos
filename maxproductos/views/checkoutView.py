from django.http import HttpResponse
from django.shortcuts import render
from maxproductos.models import Proveedor, Producto, Usuario, Carro

def verCheckout(request):
    return render(request, 'checkout.html')