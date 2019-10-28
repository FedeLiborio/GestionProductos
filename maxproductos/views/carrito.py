from django.http import HttpResponse
from django.shortcuts import render, redirect
from maxproductos.models import Proveedor, Producto, Usuario, Carro, MetodoDePago
from maxproductos.forms import *

#declaro algunos productos y proveedores
carrito = []

carritoId = []

proveedor1 = Proveedor()
proveedor1.nombre = "proveedor1"

proveedor2 = Proveedor()
proveedor2.nombre = "proveedor2"

producto1 = Producto()
producto1.nombre = "producto111"
producto1.proveedor = proveedor1
producto1.valor = 9.99

producto2 = Producto()
producto2.nombre = "producto2"
producto2.proveedor = proveedor1
producto2.valor = 9.99

producto3 = Producto()
producto3.nombre = "producto3"
producto3.proveedor = proveedor2
producto3.valor = 9.99

carrito.append(producto1)
carrito.append(producto2)
carrito.append(producto3)

##finalizo declaracion



def verCarrito(request):
    proveedores = []
    total = 0
    for p in carrito:
        if not(p.proveedor in proveedores):
            proveedores.append(p.proveedor)
        total = total + p.valor
    request.session['fav_color'] = 'blue'
    return render(request, "verCarrito.html", {"elCarrito": carrito, "losProveedores": proveedores, "total": total, "elCarritoId": carritoId})

def verCheckout(request):
    pagos = MetodoDePago.objects.all().values()
    checkoutFormulario = CheckoutForm()
    fav_color = request.session['fav_color']
    return render(request, 'checkout.html', {'losPagos': pagos, "elCarrito": carrito, "elCarritoId": carritoId, "formito": checkoutFormulario, "color": fav_color })

def agregarProducto(request):
    carritoId.append(MetodoDePago.objects.filter(nombre = "Efectivo"))
    return redirect('checkout.html')