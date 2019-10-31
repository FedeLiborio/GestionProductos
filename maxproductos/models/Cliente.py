from django.db import models
from .Usuario import Usuario

class Cliente(Usuario): 

    def __str__(self):
        return self.nombre  