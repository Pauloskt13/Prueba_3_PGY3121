from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import agregar_producto, eliminar_prod, eliminar_producto, index, inicio
from .views import limpiar_carrito, nosotros, restar_producto, tienda, contacto 
from .views import donaciones, administrador,agregar_prod,modificar_prod,lista_personas
from .views import agregar_fundacion, admin_fund,modificar_fundacion,eliminar_fundacion,\
    listar_carrito, donar, registro
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView #new

urlpatterns = [
    path('', index,name="index"),
    path('inicio', inicio,name="inicio"),
    path('nosotros', nosotros,name="nosotros"),
    path('tienda', tienda,name="tienda"),
    path('contacto', contacto,name="contacto"),
    path('donaciones', donaciones,name="donaciones"),
    path('donar', donar, name="donar"),
    path('administrador', administrador,name="administrador"),
    path('agregar_prod', agregar_prod,name="agregar_prod"),
    path('modificar_prod', modificar_prod,name="modificar_prod"),
    path('eliminar_prod', eliminar_prod,name="eliminar_prod"),
    path('lista_personas', lista_personas,name="lista_personas"),
    path('agregar_fundacion', agregar_fundacion,name="agregar_fundacion"),
    path('admin_fund',admin_fund,name="admin_fund"),
    path('modificar_fundacion',modificar_fundacion,name="modificar_fundacion"),
    path('eliminar_fundacion',eliminar_fundacion ,name="eliminar_fundacion "),
    path('listar_carrito',listar_carrito, name="listar_carrito"),
    path('agregar/<codProducto>/',agregar_producto,name="Add"),
    path('eliminar/<codProducto>/',eliminar_producto,name="Del"),
    path('restar/<codProducto>/',restar_producto,name="Sub"),
    path('limpiar/',limpiar_carrito,name="CLS"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro',registro,name="registro"), 

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)