from rest_framework import serializers
from core.models import Producto
class ProductoSerializers (serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codProducto','nombreProducto', 'descripcion','stock', 'precio','categoria', 'fotoProd']