
from django.shortcuts import redirect, render
from core.forms import ProductoForm
from .models import Producto

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')
    
def tienda(request):
    return render(request, 'core/tienda.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def donaciones(request):
    return render(request, 'core/donaciones.html')

#funciones administrador 

def administrador(request):
    productos = Producto.objects.all()

    datos = {
        'productos' : productos
    }
    return render(request, 'core/administrador.html', datos)

def agregar_prod(request):
    datos = {
        'form' : ProductoForm
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Producto Guardado Correctamente'

    return render(request, 'core/agregar_prod.html', datos)

def modificar_prod(request, id):
    producto = Producto.objects.get(codProducto = id)

    datos = {
        'form':ProductoForm(instance= producto )
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)

        if formulario.is_valid:
             formulario.save()
             datos['mensaje'] = 'Producto Modificado Correctamente'
    
    return render(request, 'core/modificar_prod.html', datos)

def eliminar_prod(request, id):
    producto = Producto.objects.get(codProducto = id)

    producto.delete()

    return redirect(to=administrador)

    

