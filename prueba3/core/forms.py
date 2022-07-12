from pyexpat import model
from attr import field, fields
from django import forms
from django.forms import ModelForm
from .models import Detalle, Fundacion, Producto
from .models import Contacto, formD, Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(ModelForm):
    imagenProd = forms.ImageField(required=False)

    class Meta: 
        model = Producto
        fields = ['codProducto','nombreProducto', 'descripcion','stock', 'precio', 'categoria','imagenProd' ]


class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        #fields = ['codFormu','nombreF','apellidoF','mailF','phoneF', 'direccionF','regionF','comunaF']
        fields = ['codFormu', 'nombreF','apellidoF','mailF','phoneF', 'direccionF']


class FundacionForm(ModelForm):
    imgFundacion = forms.ImageField(required=False)

    class Meta:
        model = Fundacion
        #fields ['nomFundacion', 'nomFundacion', 'descFundacion' , 'dirFundacion ', 'telFundacion', 'mailFundacion',','imgFundacion' ]
        fields = "__all__"

class ContactoDona(forms.ModelForm):

    class Meta:
        model = formD
        fields = ['nombreD', 'apellidoD','mailD','rutD','digito','direccionD','correo','monto','tipoCuenta','banco','fundacion']

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields ="__all__"


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

class DetalleForm(forms.ModelForm):
    
    class Meta:
        model = Detalle
        #fields = ['codFormu','nombreF','apellidoF','mailF','phoneF', 'direccionF','regionF','comunaF']
        fields =  ['total']