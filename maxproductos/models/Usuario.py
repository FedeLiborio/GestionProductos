from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.BigIntegerField()
    email = models.EmailField()
    nombreUsuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)

    class Meta:
        abstract = True