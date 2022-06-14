from rest_framework import serializers

from core.models import Producto , Fundacion

class ProductoSerializers (serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codProducto','nombreProducto', 'descripcion','stock', 'precio','categoria']

class FundacionSerializers (serializers.ModelSerializer):
    class Meta:
        model = Fundacion
        fields = ['idFundacion' , 'nomFundacion' , 'dFundacion' , 'emailFundacion' , 'telFundacion']