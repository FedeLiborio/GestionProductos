import pandas as pd

datos= pd.read_csv('Proveedor.csv',header=0)
datos1= pd.read_csv('TipoProducto.csv',header=0)
datos2= pd.read_csv('Producto.csv',header=0)


print (datos2)

print (datos2['Nombre'][0])
print (datos2['Nombre'][1])


