from django import forms
from django.forms import ModelForm
from .models import Producto


class ProductoForm(ModelForm):
    
    class Meta: 
        model = Producto
        fields = ['codProducto','nombreProducto', 'descripcion','stock', 'precio', 'categoria', ]


