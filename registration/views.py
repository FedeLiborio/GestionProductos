from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .form import ProveedorUserForm, ClienteUserForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from maxproductos.models import Proveedor, Cliente
from django.contrib.auth.views import LoginView


def registrar_usuario_proveedor_v(request):

    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_user_proveedor = ProveedorUserForm(request.POST)
        if form_user.is_valid() and form_user_proveedor.is_valid():
            print(request.POST)

            #username= form_user.cleaned_data['username']
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            calle = request.POST.get('calle')
            numero = request.POST.get('numero')
            latitud = request.POST.get('latitud')
            longitud = request.POST.get('longitud')
            telefono = request.POST.get('telefono')
            descripcionNegocio = request.POST.get('descripcionNegocio')
            calificacion = request.POST.get('calificacion')

            user = User.objects.create_user(username, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            user = User.objects.last()
            user_proveedor = Proveedor()
            user_proveedor.user = user
            user_proveedor.calle = calle
            user_proveedor.numero = numero
            user_proveedor.latitud = latitud
            user_proveedor.longitud = longitud
            user_proveedor.telefono = telefono
            user_proveedor.descripcionNegocio = descripcionNegocio
            user_proveedor.calificacion = calificacion
            user_proveedor.save()
            # sreturn render(request, 'maxproductos/mostrar_Catalogo.html')
            return redirect(reverse_lazy('/'))
    else:
        form_user = UserForm()
        form_user_proveedor = ProveedorUserForm()
        context = {'form_user': form_user,
                   'form_user_proveedor': form_user_proveedor}

    return render(request, 'registration/registrar_usuario_proveedor.html', context)


def registrar_usuario_cliente_v(request):

    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_user_cliente = ClienteUserForm(request.POST)
        if form_user.is_valid() and form_user_cliente.is_valid():
            print(request.POST)

            #username= form_user.cleaned_data['username']
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            calle = request.POST.get('calle')
            numero = request.POST.get('numero')
            latitud = request.POST.get('latitud')
            longitud = request.POST.get('longitud')
            telefono = request.POST.get('telefono')

            user = User.objects.create_user(username, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            user = User.objects.last()
            user_cliente = Cliente()
            user_cliente.user = user
            user_cliente.calle = calle
            user_cliente.numero = numero
            user_cliente.latitud = latitud
            user_cliente.longitud = longitud
            user_cliente.telefono = telefono
            user_cliente.save()
            return redirect(reverse_lazy('/'))
    else:
        form_user = UserForm()
        form_user_cliente = ClienteUserForm()
        context = {'form_user': form_user,
                   'form_user_cliente': form_user_cliente}

    return render(request, 'registration/registrar_usuario_cliente.html', context)


# class RegistrarUsuario(CreateView):
#     model = User
#     template_name= 'registration/regitrar_usuario.html'
#     form_class = ProveedorUserForm
#     success_url = reverse_lazy('/')