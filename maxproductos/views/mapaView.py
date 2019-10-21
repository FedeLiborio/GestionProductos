from django.http import HttpResponse
from django.shortcuts import render

def verMapa(request):
    return render(request, 'verMapa.html')