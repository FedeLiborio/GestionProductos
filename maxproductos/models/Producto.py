from django.db import models
from .TipoProducto import TipoProducto
from .Proveedor import Proveedor
from .Carro import Carro
from .Pedido import Pedido

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(
        TipoProducto,
        on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    valor = models.DecimalField
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete = models.CASCADE)
    carro = models.ForeignKey(
        Carro,
        on_delete=models.CASCADE)
    pedido = models.ForeignKey(
        Pedido, 
        on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre