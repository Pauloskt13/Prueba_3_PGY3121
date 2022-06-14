from django.urls import path 
from .views import eliminar_prod, index,nosotros, tienda, contacto, donaciones, administrador,agregar_prod,modificar_prod

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
]