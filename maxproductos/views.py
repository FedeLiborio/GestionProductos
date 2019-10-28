from django.shortcuts import render
#from django.views.generic.base import TemplateView
from maxproductos.models.Producto import Producto
from .form import ProveedorForm

lista=[]

# def agregar_lista(request,id):
#     lista.append(id)


# class MostrarCatalogoView(TemplateView):
#     template_name = "maxproductos/mostrar_catalogo.html"

#     def get(self, request, *args, **kwargs)
#     return render(request, self.template_name, {'sd': 'asd'})


def mostrar_catalogo_v(request):
    print(request.get_host())
    list_Producto = Producto.objects.all()
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
    
    return render (request, 'maxproductos/detalle_producto.html',{'producto':producto})