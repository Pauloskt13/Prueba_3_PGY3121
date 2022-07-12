from django.contrib import admin
from .models import CategoriaProd, Detalle, Fundacion, Producto, Contacto, formD, estadoPedido, pedido, promo
from .models import Usuario
# Register your models here.

admin.site.register(CategoriaProd)
admin.site.register(Producto)
admin.site.register(Contacto)
admin.site.register(Fundacion)
admin.site.register(formD)
admin.site.register(estadoPedido)
admin.site.register(pedido)
admin.site.register(promo)
admin.site.register(Usuario)
admin.site.register(Detalle)
