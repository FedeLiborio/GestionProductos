from django.db import models
from .Usuario import Usuario

class Proveedor(Usuario):
    #horariosDeEntrega
    descripcionNegocio = models.CharField(max_length=200)
    calificacion = models.IntegerField

    def __str__(self):
        return self.nombre 