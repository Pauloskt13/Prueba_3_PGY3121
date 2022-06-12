from ast import parse
from os import stat
from django.shortcuts import render
from urllib import request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto
from .serializers import ProductoSerializers

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_productos(request):
    """
    GET = lista todos los productos
    POST = Agregar registro
    """
    if request.method == 'GET':
        Producto = Producto.objects.all()
        serializer = ProductoSerializers(Producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


