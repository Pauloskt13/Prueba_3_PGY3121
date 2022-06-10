from django.shortcuts import render

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

def administrador(request):
    return render(request, 'core/administrador.html')