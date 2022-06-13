from distutils.command.upload import upload
from django.db import models



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
    fotoProd = models.ImageField(upload_to='static/img/',null=True)
    categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)


    def __int__(self):
        return self.codProducto






    
      
    

    
    
    