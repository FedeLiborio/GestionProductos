from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

#probar cuando edite un proveedor
# class ProveedorInline(admin.StackedInline):
#     model = Proveedor
#     can_delete = False
#     verbose_name_plural = 'proveedor'

# class UserAdmin(BaseUserAdmin):
#     inlines = (ProveedorInline,)    

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado',)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

admin.site.register(Horario)
admin.site.register(Proveedor)
admin.site.register(MetodoDePago)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Administrador)
admin.site.register(TipoProducto)
#admin.site.register(Producto)
admin.site.register(Producto, ProductoAdmin)

