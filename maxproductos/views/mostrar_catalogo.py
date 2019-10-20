from django.shortcuts import render
from maxproductos.models.Producto import Producto

def mostrar_catalogo(request):
    list_Producto= Producto.objects.all()
    return render(request, 'maxproductos/mostrar_catalogo.html',{"objproducto":list_Producto})
