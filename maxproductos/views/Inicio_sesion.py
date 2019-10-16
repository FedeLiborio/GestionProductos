from django.shortcuts import render

def iniciar_sesion(request):
    return render(request, 'maxproductos/inicio_sesion.html')
