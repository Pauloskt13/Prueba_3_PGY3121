from django.urls import path 
from .views import index,nosotros, tienda, contacto, donaciones, administrador, agregar_prod, modificar_prod, eliminar_prod,agregar_fund,modificar_fund,eliminar_fund

urlpatterns = [
    path('', index,name="index"),
    path('', nosotros,name="nosotros"),
    path('', tienda,name="tienda"),
    path('', contacto,name="contacto"),
    path('', donaciones,name="donaciones"),
    path('', administrador,name="administrador"),
    path('', agregar_prod,name="agregar_prod"),
    path('', modificar_prod,name="modificar_prod"),
    path('', eliminar_prod,name="eliminar_prod"),
    path('', agregar_fund,name="agregar_fund"),
    path('', modificar_fund,name="modificar_fund"),
    path('', eliminar_fund,name="eliminar_fund"),
]

