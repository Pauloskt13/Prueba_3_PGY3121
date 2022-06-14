from django.urls import path
from .views import lista_productos , lista_fundaciones

urlpatterns = [
    path('lista_productos', lista_productos, name="lista_productos"),
    path('lista_fundaciones',lista_fundaciones,name='lista_fundaciones'),
]