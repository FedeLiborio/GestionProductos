from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_lenght=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_lenght=100)
    telefono = models.BigIntegerField()
    email = models.EmailField()
    nombreUsuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)

class Proveedor(Usuario):
    #horariosDeEntrega
    descripcionNegocio = models.CharField(max_lenght=200)
    calificacion = models.IntegerField

class Cliente(Usuario):
    #buscar sobre uno a uno e implementar
    carro = models.ForeignKey(
        'Carro',
        on_delete=models.CASCADE,)

class Administrador(Usuario):
    pass

class Producto(models.Model):
    nombre = models.CharField(max_lenght=50)
    tipo = models.ForeignKey(
        'TipoProducto',
        on_delete=models.CASCADE)
    descripcion = models.CharField(max_lenght=200)
    valor = models.DecimalField
    proveedor = models.ForeignKey(
        'Proveedor',
        on_delete = models.CASCADE)
    carro = models.ForeignKey(
        'Carro',
        on_delete=models.CASCADE)
    pedido = models.ForeignKey(
        'Pedido', 
        on_delete = models.CASCADE)

class TipoProducto(models.Model):
    nombre = models.CharField(max_lenght=50)

class Carro(models.Model):
    #listaProductos
    metodoDePago = models.ForeignKey(
        'MetodoDePago',
        on_delete=models.CASCADE)

class MetodoDePago(models.Model):
    nombre = models.CharField(max_length=50)

class Pedido(models.Model):
    #tiene una lista de productos
    
    confirmado = models.BooleanField()
    #cuando confirmado = true, el pedido pasa a la lista de pedidos para entregar
    
    cliente = models.ForeignKey(
        'Cliente',
        on_delete = models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    proveedor = models.ForeignKey(
        'Proveedor', 
        on_delete=models.CASCADE)
    direccion = models.CharField(max_lenght=100)
    entregado = models.BooleanField()

class Horario(models.Model):
    horaInicio = models.IntegerField()
    horaFinal = models.IntegerField()
    dia = models.CharField(max_length=15)