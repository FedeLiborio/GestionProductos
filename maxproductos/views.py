from django.shortcuts import render
#from django.views.generic.base import TemplateView
from maxproductos.models import Producto, Proveedor, Producto, Usuario, MetodoDePago
from .form import ProveedorForm

lista=[]

# def agregar_lista(request,id):
#     lista.append(id)


# class MostrarCatalogoView(TemplateView):
#     template_name = "maxproductos/mostrar_catalogo.html"

#     def get(self, request, *args, **kwargs)
#     return render(request, self.template_name, {'sd': 'asd'})


def mostrar_catalogo_v(request):
    list_Producto = Producto.objects.all()
    if 'carrito' not in request.session:
        request.session['carrito'] = [] 

    if (request.method == 'GET'):
        if 'elId' in request.GET:
            dic= request.GET # devuelve un diccionario
            id = dic['elId']
            id = int(id)
            #id= int(dic['elId'])

            print(type(id))
            carritoAux= request.session['carrito']
            if id  not in carritoAux:
                carritoAux.append(id) 
            request.session['carrito']= carritoAux

    return render(request, 'maxproductos/mostrar_catalogo.html', {"objproducto": list_Producto, "carrito": lista})


def iniciar_sesion_v(request):
    return render(request, 'maxproductos/iniciar_sesion.html')


def registrar_usuario_v(request):
    formulario_proveedor = ProveedorForm()
    # print(request.POST)
    return render(request, 'maxproductos/registrar_usuario.html', {'formulario': formulario_proveedor})

def detalle_producto_v(request, idProducto):
    producto= Producto.objects.get(id=idProducto)
    #producto= Producto.objects.filter(id=id)
    
    return render (request, 'maxproductos/detalle_producto.html',{'producto':producto,'carrito':request.session['carrito']})


##################################################################################################

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

    return render(request, "maxproductos/verCarrito.html", {"elCarrito": productosAgregados, "losProveedores": proveedores, "total": total})

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

    return render(request, 'maxproductos/checkout.html', {'losPagos': pagos, "elCarrito": carrito, "elCarritoId": carritoId, "formito": checkoutFormulario, "listita": lista, 'metodo': metodo, 'rq': rq})

def verMapa(request):
    return render(request, 'maxproductos/verMapa.html')

