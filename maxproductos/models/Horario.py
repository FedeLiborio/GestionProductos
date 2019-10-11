from django.db import models
from .Proveedor import Proveedor

class Horario(models.Model):
    horaInicio = models.IntegerField()
    horaFinal = models.IntegerField()
    dia = models.CharField(max_length=15)
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.horaInicio