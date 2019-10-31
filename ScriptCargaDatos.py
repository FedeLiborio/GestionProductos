import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'repartidor.settings')
django.setup()

from maxproductos.models.Proveedor import Proveedor
from maxproductos.models.TipoProducto import TipoProducto
from maxproductos.models.Producto import Producto


with open ('Proveedor.json','r') as archivo:
    proveedor= archivo.read()

objeto= json.loads(proveedor)
#print (objeto)

for it in objeto:
    p = Proveedor()
    p.nombre = it['Nombre']
    p.apellido = it['Apellido']
    p.direccion = it['Direccion']
    p.telefono = it['Telefono']
    p.email = it['Email']
    p.nombreUsuario = it['NombreUsuario']
    p.contrasenia = it['Contrasenia']
    p.descripcionNegocio = it['DescripcionNegocio']
    p.calificacion = 0
    p.save()
print('TERMINADO')