from django.contrib import admin
from .models import *

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado',)

admin.site.register(Horario)
admin.site.register(Proveedor)
admin.site.register(MetodoDePago)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Administrador)
admin.site.register(TipoProducto)
#admin.site.register(Producto)
admin.site.register(Producto, ProductoAdmin)

