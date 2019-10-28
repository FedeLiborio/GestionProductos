from django.db import models
from .Cliente import Cliente
from .Proveedor import Proveedor
from .MetodoPago import MetodoDePago

class Pedido(models.Model):
    #tiene una lista de productos
    
    confirmado = models.BooleanField()
    #cuando confirmado = true, el pedido pasa a la lista de pedidos para entregar
    
    cliente = models.ForeignKey(
        Cliente,
        on_delete = models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    proveedor = models.ForeignKey(
        Proveedor, 
        on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    entregado = models.BooleanField()
    metodoDePago = models.ForeignKey(
        MetodoDePago,
        on_delete = models.CASCADE)
