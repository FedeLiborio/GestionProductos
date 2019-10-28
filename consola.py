import os
import django
import pandas as pd
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'repartidor.settings')
django.setup()

from maxproductos.models.Proveedor import Proveedor
from maxproductos.models.TipoProducto import TipoProducto
from maxproductos.models.Producto import Producto

# it = pd.read_csv('Proveedor.csv', header=0)
# it1 = pd.read_csv('TipoProducto.csv', header=0)
# it2 = pd.read_csv('Producto.csv', header=0)

# for i in range(len(it)):
#     p = Proveedor()
#     p.nombre = it['Nombre']
#     p.apellido = it['Apellido']
#     p.direccion = it['Direccion']
#     p.telefono = pd.to_numeric(it['Telefono'])
#     p.email = it['Email']
#     p.nombreUsuario = it['NombreUsuario']
#     p.contrasenia = it['Contrasenia']
#     p.descripcionNegocio = it['DescripcionNegocio']
#     p.calificacion = 0
#     p.save()

    # print(it['Nombre'][i])
    # print(it['Apellido'][i])
    # print(it['Telefono'][i])


# print (Producto.objects.all())

# tp= TipoProducto(nombre='Ropa')
# tp.save()
# tp= TipoProducto()
# tp.nombre= 'Ropa'
# tp.save()

# with open('Proveedor.csv', 'r') as archivo:
#     a= archivo.read().splitlines()
#     # titulo= a[0]
#     # print(titulo)
#     # print(a)
#     for l in a:
#         a= l.split(',')
#         print(a)

# results = []
# with open('Proveedor.csv') as File:
#     reader = csv.DictReader(File)
#     for row in reader:
#         results.append(row)
#     print (results)
########################################################
import json

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