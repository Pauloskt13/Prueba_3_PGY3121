
from core.forms import ProductoForm , FundacionForm
from .models import Producto, Fundacion
from django.shortcuts import render, redirect  
from distutils.command.upload import upload
from asyncio.windows_events import NULL


# Create your views here.

# Vistas Secciones 
def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')
    

def tienda(request):
    Productos = Producto.objects.all()

    data={
        'productos':Productos
    }

    return render(request, 'core/tienda.html', data)

def contacto(request):
    return render(request, 'core/contacto.html')

def donaciones(request):
    Fundaciones = Fundacion.objects.all()

    datos={
        'fundaciones': Fundaciones
    }
    
    
    return render(request, 'core/donaciones.html', datos)


#VISTAS DE ADMINISTRADOR PRODUCTOS  

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

        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado Correctamente'

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


# def administrador(request):
#     fundaciones = Fundacion.objects.all()

#     datos = {
#         'fundaciones' : fundaciones
#     }
    return render(request, 'core/administrador.html', datos)

def agregar_fund(request):
    datos = {
        'form' : FundacionForm
    }

    if request.method == 'POST':
        formulario_fundacion = FundacionForm(request.POST)

        if formulario_fundacion.is_valid():
            formulario_fundacion.save()
            datos['mensaje'] = 'Guardado Correctamente'

    return render(request, 'core/agregar_fund.html', datos)

def modificar_fund(request, id):
    fundacion = Fundacion.objects.get(idFundacion = id)

    datos = {
        'form':FundacionForm(instance= fundacion )
    }

    if request.method == 'POST':
        formulario_fundacion = FundacionForm(data=request.POST, instance=fundacion)

        if formulario_fundacion.is_valid:
             formulario_fundacion.save()
             datos['mensaje'] = 'Fundacion Modificada Correctamente'
    
    return render(request, 'core/modificar_fund.html', datos)

def eliminar_fund(request, id):
    fundacion = Fundacion.objects.get(idFundacion = id)

    fundacion.delete()

    return redirect(to=administrador)
    