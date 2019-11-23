from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from maxproductos.models import Proveedor, Cliente


class UserForm (UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']


class ProveedorUserForm(ModelForm):
    class Meta:
        model = Proveedor # ME VIVO AUTO CAGANDOOOOOO
        exclude = ['user']

class ClienteUserForm(ModelForm):
    class Meta:
        model = Cliente # ME VIVO AUTO CAGANDOOOOOO
        exclude = ['user']