from django.shortcuts import render


def mostrar_catalogo(request):
    return render(request, 'maxproductos/mostrarCatalogo.html')
