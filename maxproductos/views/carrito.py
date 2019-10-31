from django.http import HttpResponse
from django.shortcuts import render, redirect
from maxproductos.models import Proveedor, Producto, Usuario, Carro, MetodoDePago
from maxproductos.forms import *

#declaro algunos productos y proveedores
carrito = []


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
    #me aseguro que el carrito exista en la session, por las dudas
    if 'carrito' not in request.session:
        request.session['carrito'] = []
    
    carritoAux = request.session['carrito']
    carritoAux.append(1)
    #traigo todos los productos existentes
    productosQuerySet = Producto.objects.all()

    #inicializo las variables que voy a pasar al template
    productosAgregados = []
    proveedores = []
    total = 0

    #guardo los objetos Producto dentro de productosAgregados y extraigo los proveedores
    for producto in productosQuerySet:
        if producto.id in carritoAux:
            productosAgregados.append(producto)
            if not(Proveedor.objects.get(id=producto.proveedor) in proveedores):
                proveedores.append(Proveedor.objects.get(id=producto.proveedor))
            #total = total + producto.valor

    return render(request, "verCarrito.html", {"elCarrito": productosAgregados, "losProveedores": proveedores, "total": total})




def verCheckout(request):
    pagos = MetodoDePago.objects.all().values()


    
    rq = request.GET.get('id', False)
    if rq != False:
        rq = int(rq)
    checkoutFormulario = CheckoutForm()
    if 'lista' not in request.session:
        request.session['lista'] = []
   
    listaAux = request.session['lista']
    listaAux.append(0)
    request.session['lista'] = listaAux
    lista = request.session['lista']
    metodo = request.method

    return render(request, 'checkout.html', {'losPagos': pagos, "elCarrito": carrito, "elCarritoId": carritoId, "formito": checkoutFormulario, "listita": lista, 'metodo': metodo, 'rq': rq})

def agregarProducto(request):
    carritoId.append(MetodoDePago.objects.filter(nombre = "Efectivo"))
    return redirect('checkout.html')