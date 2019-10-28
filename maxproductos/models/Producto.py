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
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete = models.CASCADE)
    pedido = models.ForeignKey(
        Pedido, 
        on_delete = models.CASCADE, null= True, blank= True)

    creado= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre