from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from asyncio.windows_events import NULL
from distutils.command.upload import upload
from tkinter.tix import INCREASING




# Create your models here.


class CategoriaProd(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria Proucto')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    codProducto = models.IntegerField(primary_key=True, verbose_name='Codigo Producto')
    nombreProducto = models.CharField(max_length=50, verbose_name="Nombre producto")
    descripcion = models.CharField(max_length=50, verbose_name="Descripccion Producto")
    stock = models.IntegerField(verbose_name="Cantidad Disponible")
    precio = models.IntegerField( verbose_name="Precio Producto")
    # imagenProd = models.ImageField(upload_to='core/static/img',null=True)
    categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)

    def __int__(self):
        return self.codProducto

class TipoFundacion(models.Model):
    idTipocat = models.IntegerField(primary_key=True, verbose_name='Id de Categoria Proucto')
    nomCat = models.CharField(max_length=50,verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nomCat


class Fundacion(models.Model):
    idFundacion = models.IntegerField(primary_key=True,verbose_name='Id Fundacion')
    nomFundacion= models.CharField(max_length=50, verbose_name='Nombre Fundacion')
    dFundacion = models.CharField(max_length=50, verbose_name='Direccion Fundacion')
    emailFundacion = models.CharField(max_length=50, verbose_name='Email Fundacion')
    telfundacion = models.CharField(max_length=15, verbose_name='Telefono fundacion')

    def __int__(self):
        return self.idFundacion






    
      
    

    
    
    