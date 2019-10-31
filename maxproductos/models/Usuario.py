from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    calle= models.CharField(max_length=100)
    numero= models.IntegerField()
    latitud = models.DecimalField(max_digits=20, decimal_places=10)
    longitud = models.DecimalField(max_digits=20, decimal_places=10)
    
    telefono = models.BigIntegerField()
    email = models.EmailField()
    nombreUsuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)