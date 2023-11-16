from django.contrib import admin
from MisApps.Productos.models import Producto
from MisApps.Productos.models import TipoProducto

# Register your models here.
admin.site.register (Producto)
admin.site.register (TipoProducto)