from .models import Producto

lista=[]

def agregar_lista(request,id):
     lista.append(id)

def ctx_dict(request):
    
    ctx= {"listaProduco":"hola"}
    return ctx    
