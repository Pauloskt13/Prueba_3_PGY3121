from django.contrib import admin
from .models import CategoriaProd, Fundacion, Producto, TipoFundacion

# Register your models here.

admin.site.register(CategoriaProd)
admin.site.register(Producto)
admin.site.register(Fundacion)
admin.site.register(TipoFundacion)