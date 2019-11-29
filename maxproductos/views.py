from django.shortcuts import render, redirect
#from django.views.generic.base import TemplateView
from maxproductos.models import Producto, Proveedor, Producto, MetodoDePago, Pedido, Horario, Cliente
from .form import ProveedorForm
from datetime import datetime
import calendar
from urllib.request import urlopen
import json
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from maxproductos.models import Producto, Proveedor, Producto, MetodoDePago, TipoProducto
from .form import ProveedorForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

#from django.utils.decorators import method_decarator

# class StaffRequiredMixin(object):
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_staff:
#             return redirect(reverse_lazy('admin:login'))
#         #print(request.user)
#         return super(StaffRequiredMixin,self).dispatch(request, *args, **kwargs)


# class MostrarCatalogoView(TemplateView):
#     template_name = "maxproductos/mostrar_catalogo.html"

#     def get(self, request, *args, **kwargs)
#     return render(request, self.template_name, {'sd': 'asd'})


def mostrar_catalogo_v(request):
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    list_Producto = Producto.objects.all()
    list_TipoProducto = TipoProducto.objects.all()
    list_proveedor =  Proveedor.objects.all()

    list_id_users_proveedor= []
    for it in list_proveedor:
        list_id_users_proveedor.append(it.user.id)
        #print ('asdsadasd ', it.user.id)

    if 'carrito' not in request.session:
        request.session['carrito'] = []

    
    if 'clasificacion' in request.GET:
        tipoElegido = request.GET.get('clasificacion') 
        print('tipoElegido: ', tipoElegido)

        if (tipoElegido != 'Seleccione...'):
            #print (type(tipoElegido))
            tipoElegido= int(tipoElegido)
            #print(type(tipoElegido))
            list_Producto = Producto.objects.filter(tipo = tipoElegido)
            #print ('NO 0')

    if (request.method == 'GET'):
        if 'elId' in request.GET:
            dic = request.GET  # devuelve un diccionario
            id = dic['elId']
            id = int(id)
            #id= int(dic['elId'])

            # print(type(id))
            carritoAux = request.session['carrito']
            if id not in carritoAux:
                carritoAux.append(id)
            request.session['carrito'] = carritoAux
        # if 'clasificacion' in request.GET:
        #     dic = request.GET
        #     if dic['clasificacion'] == "1":
        #         p = Producto.objects.get(id=1)
            return render(request, 'maxproductos/mostrar_catalogo.html', {"objproducto": list_Producto})            


    #tipoProductos = TipoProducto.objects.all()
    # print(tipoProductos)

    #proveedor = Proveedor.objects.all()
    # print(proveedor['Proveedor'])

    return render(request, 'maxproductos/mostrar_catalogo.html', {"objproducto": list_Producto, 'list_TipoProducto': list_TipoProducto, 'list_id_users_proveedor':list_id_users_proveedor})


def iniciar_sesion_v(request):
    return render(request, 'maxproductos/iniciar_sesion.html')


class InicioSesionView(TemplateView):
    template_name = "maxproductos/iniciar_sesion.html"

#adsasd
def registrar_usuario_v(request):
    formulario_proveedor = ProveedorForm()
    # print(request.POST)
    return render(request, 'maxproductos/registrar_usuario.html', {'formulario_proveedor': formulario_proveedor})


def detalle_producto_v(request, idProducto):
    producto = Producto.objects.get(id=idProducto)
    #producto= Producto.objects.filter(id=id)

    return render(request, 'maxproductos/detalle_producto.html', {
        'producto': producto,
        'carrito': request.session['carrito']
    })

def mostrar_perfil_proveedor_v(request):
    
    return render(request, 'registration/perfil_proveedor.html')
 
def mostrar_perfil_cliente_v(request):
    
    return render(request, 'registration/perfil_cliente.html')
    

##################################################################################################

def verCarrito(request):
    diasDeLaSemana = {0: 'Lunes', 1: 'Martes', 2: 'Miercoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sabado', 6: 'Domingo'}

    #me aseguro que el carrito exista en la session, por las dudas
    if 'carrito' not in request.session:
        request.session['carrito'] = []

    carritoAux = request.session['carrito']
    carritoAux.append(1)
    carritoAux.append(2)
    #traigo todos los productos existentes
    productosQuerySet = Producto.objects.all()

    # inicializo las variables que voy a pasar al template
    productosAgregados = []
    proveedores = []
    total = 0
    horariosProveedor = Horario.objects.all()

    # guardo los objetos Producto dentro de productosAgregados y extraigo los proveedores
    for producto in productosQuerySet:
        if producto.id in carritoAux:
            productosAgregados.append(producto)
            if not(Proveedor.objects.get(id=producto.proveedor.id) in proveedores):
                proveedores.append(Proveedor.objects.get(id=producto.proveedor.id))
            total = total + producto.valor

    if (request.method == 'GET'):
        if 'solicitudCheckout' in request.GET:
            datosValidados = True
            pedidosParaAlmacenar = []
            for prov in proveedores:
                fechaProvId = "fecha" + str(prov.id)
                tiempoProvId = "tiempo" + str(prov.id)
                
                if fechaProvId in request.GET:
                    dic= request.GET # devuelve un diccionario
                    fecha = dic[fechaProvId]
                    tiempo = dic[tiempoProvId]

                    diaDeLaSemana = datetime.strptime(fecha, '%Y-%m-%d').date().weekday()
                    diaDeLaSemana = diasDeLaSemana.get(diaDeLaSemana)

                    hora = datetime.strptime(tiempo, '%H:%M').time()

                    if diaDeLaSemana in Horario.objects.filter(proveedor = prov).values_list('dia', flat=True):
                        for h in Horario.objects.filter(proveedor = prov, dia = diaDeLaSemana).values_list('horaInicio', flat=True):
                            if(hora >= h):
                                for h in Horario.objects.filter(proveedor = prov, dia = diaDeLaSemana).values_list('horaFinal', flat=True):
                                    if(hora <= h):
                                        #Si entra en este if, la fecha y hora esta validada
                                        pedidosParaAlmacenar.append({
                                            "proveedor": prov.id,
                                            "cliente": 2,
                                            "hora": tiempo,
                                            "fecha": fecha

                                        })
                                        datosValidados = datosValidados and True
                                    else:
                                        datosValidados = datosValidados and False
                            else:
                                datosValidados = datosValidados and False
                    else:  
                        datosValidados = datosValidados and False
            if datosValidados == True:
                request.session['pedidosParaAlmacenar'] = pedidosParaAlmacenar 
                return redirect('proceder_Checkout')
            else:
                print("Datos incorrectos. Vuelva a intentar")

    return render(request, "maxproductos/verCarrito.html", {"elCarrito": productosAgregados, "losProveedores": proveedores, "total": total, "horarios": horariosProveedor})

def verCheckout(request):
    pagos = MetodoDePago.objects.all().values()

    if (request.method == 'GET'):
        if 'solicitudRealizarPedido' in request.GET:
            dic= request.GET # devuelve un diccionario
            pedidosParaAlmacenar = request.session['pedidosParaAlmacenar']
            for p in pedidosParaAlmacenar:
                cliente = Cliente.objects.get(id= p['cliente'])
                proveedor = Proveedor.objects.get(id= p['proveedor'])
                if dic['elegirDir'] == 'propia':                  
                    calleNombre = Cliente.objects.get(id= p['cliente']).calle
                    calleNumero = Cliente.objects.get(id= p['cliente']).numero
                    latitud = Cliente.objects.get(id= p['cliente']).latitud
                    longitud = Cliente.objects.get(id= p['cliente']).longitud
                else:
                    calleNombre = dic['nuevaCalle'].replace(" ","+")
                    calleNumero = dic['nuevaCalleNumero']
                    #Se envia una direccion por la url y se recibe un json con varios datos, entre ellos la latitud y longitud
                    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + calleNumero + "+" + calleNombre + "&key=AIzaSyAgnETqEf92aH6sMfZ8TT3oXpR1ZWubs0Y"
                    json_url = urlopen(url)
                    data = json.loads(json_url.read())
                    latitud = data['results'][0]['geometry']['location']['lat']
                    longitud = data['results'][0]['geometry']['location']['lng']
                    
                    calleNombre = dic['nuevaCalle'].replace("+"," ")
                pedido = Pedido(confirmado=0,fecha= p['fecha'], hora= p['hora'], calle= calleNombre, numero=calleNumero, latitud= latitud, longitud = longitud, entregado= 0, cliente= cliente, proveedor= proveedor)
                pedido.save()
                
                #Comienza a asociar los productos con el pedido
                carritoAux = request.session['carrito']

                #traigo todos los productos existentes
                productosQuerySet = Producto.objects.all()
                productosAgregados = []

                #guardo los objetos Producto dentro de productosAgregados
                for producto in productosQuerySet:
                    if producto.id in carritoAux:
                        productosAgregados.append(producto)
                for p in productosAgregados:
                    pedido.productos.add(p)
    return render(request, 'maxproductos/checkout.html', {'losPagos': pagos})

def verMapa(request):
    coordenadas=[]
    pedidosQuerySet = Pedido.objects.all()
    for p in pedidosQuerySet:
        latAux = str(p.latitud).replace(',','.')
        lngAux = str(p.longitud).replace(',','.')
        coordenadas.append({'latitud': latAux, 'longitud': lngAux})

    return render(request, 'maxproductos/verMapa.html',{'coordenadas': coordenadas})

