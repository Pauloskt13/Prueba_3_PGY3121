from django.urls import URLPattern, path
from .views import lista_productos

urlpatterns = [
    path('lista_productos', lista_productos, name="lista_productos"),
]