from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nombrecalle = models.CharField(max_length=100)
    numerocalle = models.IntegerField()
    telefono = models.BigIntegerField()
    email = models.EmailField()
    nombreUsuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)

    class Meta:
        abstract = True