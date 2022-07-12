from distutils.command.upload import upload
from doctest import register_optionflag
from pyexpat import model
from django.db import models
from asyncio.windows_events import NULL
from distutils.command.upload import upload
from tkinter.tix import INCREASING
from django.contrib.auth import get_user_model


# Create your models here.


class CategoriaProd(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name='Id de Categoria Proucto')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    codProducto = models.AutoField(primary_key=True, verbose_name='Código Producto')
    nombreProducto = models.CharField(max_length=50, verbose_name="Nombre producto")
    descripcion = models.CharField(max_length=50, verbose_name="Descripcción Producto")
    stock = models.IntegerField(verbose_name="Cantidad Disponible")
    precio = models.IntegerField( verbose_name="Precio Producto")
    imagenProd = models.ImageField(upload_to='media/img/', null=True, blank=True)
    categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)

    def __int__(self):
        return self.codProducto



class Contacto(models.Model):
    codFormu = models.AutoField(primary_key=True, verbose_name='Código Formulario')
    nombreF = models.CharField(max_length=50, verbose_name="Nombre ")
    apellidoF = models.CharField(max_length=50, verbose_name="Apellido")
    mailF = models.EmailField(verbose_name="Correo")
    phoneF = models.IntegerField( verbose_name="Teléfono")
    direccionF = models.CharField(max_length=250, null=True, blank=True, verbose_name="Dirección")
    regionF = models.CharField(max_length=250, blank=True, verbose_name='Región de Cliente')
    comunaF = models.CharField(max_length=250, blank=True, verbose_name='Comuna')
   
  
    def __str__(self):
        return self.nombreF

class Fundacion(models.Model):
    codFundacion = models.AutoField(primary_key=True, verbose_name="Código Fundación")
    nomFundacion = models.CharField(max_length=50,verbose_name="Nombre Fundación")
    descFundacion = models.CharField(max_length=200, verbose_name="Descripción Fundación")
    dirFundacion = models.CharField(max_length=50,verbose_name="Dirección Fundación")
    telFundacion = models.IntegerField(verbose_name="Teléfono Contacto")
    mailFundacion = models.EmailField(verbose_name="Correo")
    imgFundacion = models.ImageField(upload_to='media/img/', null=True, blank=True)

    def __int__(self):
        return self.codFundacion


opciones_cuenta = [
    [1, "cuenta vista"],
    [2, "cuenta corriente"]
]

opciones_banco = [
    [1, "Banco Estado"],
    [2, "Banco Chile"],
    [3, "Banco Falabella"],
    [4, "Banco Itau"],
    [5, "Banco Scotiebank"],
    [6, "Banco Santander"],
    [7, "Banco BCI"]
]

opciones_funda = [
    [1, "Callejeros buscan hogar"],
    [2, "Fundación Julieta"],
    [3, "Garras & patas"],
    [4, "Fundación Julieta"]
]

class formD(models.Model):
    codFormuD = models.AutoField(primary_key=True, verbose_name='Codigo Formulario')
    nombreD = models.CharField(max_length=50, verbose_name="Nombre ")
    apellidoD = models.CharField(max_length=50, verbose_name="Apellido")
    mailD = models.EmailField(verbose_name="Correo")
    rutD = models.IntegerField( verbose_name="Rut")
    digito = models.CharField(max_length=1, verbose_name="digito")
    direccionD = models.CharField(max_length=250, null=True, blank=True, verbose_name="Dirección")
    correo = models.EmailField(verbose_name="Correo")
    monto = models.IntegerField(verbose_name="Monto")
    tipoCuenta = models.IntegerField(choices=opciones_cuenta, verbose_name="Tipo cuenta")
    banco = models.IntegerField(choices=opciones_banco, verbose_name="Banco")
    fundacion = models.IntegerField(choices=opciones_funda, verbose_name="Nombre de la fundación")

    def __int__(self):
        return self.codFormuD

# seguimiento - DELIVERY estados enviado - por despachar . en ruta - en preparación 
class estadoPedido(models.Model):
    codigo = models.IntegerField(primary_key=True, verbose_name="código")
    descripcion = models.CharField(max_length=20, verbose_name="Estado")

    def __int__(self):
        return self.codigo   


# carrito de compras
class pedido(models.Model):
    codPedido = models.AutoField(primary_key=True, verbose_name="Código compra")
    fechaPedido = models.DateField(verbose_name="Fecha Compra")
    fechaPago = models.DateField(verbose_name="Fecha pago")
    tipoPedido = models.IntegerField( verbose_name="Tipo de compra")
    codFactura = models.IntegerField(verbose_name="Código factura")
    totalPedido = models.IntegerField(verbose_name="Total")
    estadoPedido = models.ForeignKey(estadoPedido, on_delete=models.CASCADE)
    #codUsuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    
    def __int__(self):
        return self.codPedido

class promo(models.Model):
    codPromo = models.IntegerField(verbose_name="Código promoción")
    descripcionP = models.CharField(max_length=20, verbose_name="Descripción")
    descuento = models.IntegerField(verbose_name="descuento")

class Usuario(models.Model):
    codUser = models.AutoField(primary_key=True, verbose_name="Codigo Usuario")
    nombre = models.CharField(max_length=50,verbose_name="Nombre")
    apellido = models.CharField(max_length=50,verbose_name="Apellido ")
    mailUser = models.EmailField(verbose_name="Correo Electronico")
    telefono = models.IntegerField(verbose_name="Telefono User")
    nombreUser = models.CharField(max_length=50, verbose_name="Nombre de Usuario")
    passUser = models.CharField(max_length=50,verbose_name="Contraseña Usuario")

    def __int__(self):
        return self.codUser    


# mostrar total , fecha y usuario
User=get_user_model()

class Detalle(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    total=models.IntegerField( verbose_name="Precio total")

    def __str__(self):
        return self.user

