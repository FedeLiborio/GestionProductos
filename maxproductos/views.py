from django.shortcuts import render


def mostrar_catalogo(request):
    #listaProductos= Producto.objectes.all()
    return render(request, 'maxproductos/mostrarCatalogo.html')
