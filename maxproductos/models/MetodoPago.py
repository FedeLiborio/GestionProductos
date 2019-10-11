from django.db import models

class MetodoDePago(models.Model):
    nombre = models.CharField(max_length=50)
