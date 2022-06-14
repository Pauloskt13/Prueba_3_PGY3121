from django import forms
from django.forms import ModelForm
from .models import  Fundacion, Producto


class ProductoForm(ModelForm):
    
    class Meta: 
        model = Producto
        fields = ['codProducto','nombreProducto', 'descripcion','stock', 'precio', 'categoria']

class FundacionForm(ModelForm):
    class Meta:
        model = Fundacion
        fields = ['idFundacion' , 'nomFundacion' , 'dFundacion' , 'emailFundacion' , 'telfundacion']
