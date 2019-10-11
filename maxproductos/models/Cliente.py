from django.db import models
from .Carro import Carro
from .Usuario import Usuario

class Cliente(Usuario):
    carro = models.ForeignKey(
        Carro,
        on_delete=models.CASCADE,)

    def __str__(self):
        return self.nombre  