import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'repartidor.settings')
django.setup()

from maxproductos.models.Producto import Producto
from maxproductos.models.TipoProducto import TipoProducto
from maxproductos.models.Proveedor import Proveedor

with open('Proveedor.json', 'r') as archivoProveedor:
    proveedor = archivoProveedor.read()
objetoProveedor = json.loads(proveedor)

with open('TipoProducto.json', 'r') as archivoTipoProducto:
    tipoProducto = archivoTipoProducto.read()
objetoTipoProducto = json.loads(tipoProducto)

with open('Producto.json', 'r') as archivoProducto:
    producto = archivoProducto.read()
objetoProducto = json.loads(producto)


#print (objeto)

for it in objetoTipoProducto:
    tp = TipoProducto()
    tp.nombre = it['Nombre']
    tp.save()

for it in objetoProveedor:
    p = Proveedor()
    #p.user = 
    p.nombre = it['Nombre']
    p.apellido = it['Apellido']
    p.calle = it['Calle']
    p.numero = it['Numero']
    p.latitud = it['Latitud']
    p.longitud = it['Longitud']
    p.telefono = it['Telefono']
    p.email = it['Email']
    p.nombreUsuario = it['NombreUsuario']
    p.contrasenia = it['Contrasenia']
    p.descripcionNegocio = it['DescripcionNegocio']
    p.calificacion = 0
    p.save()

dicTipo= TipoProducto.objects.all()
pro= Proveedor.objects.all()

for it in objetoProducto:
    p = Producto()
    p.nombre = it['Nombre']
    p.marca = it['Marca']
    
    for tp in dicTipo:
        if it['Tipo'] == tp.nombre:
            p.tipo= tp 
        
    p.descripcion = it['Descripcion']
    p.valor = it['Valor']

    for pr in pro:
        if it['Proveedor'] == pr.nombre:
            p.proveedor= pr
    p.save()

print('TERMINADO')
