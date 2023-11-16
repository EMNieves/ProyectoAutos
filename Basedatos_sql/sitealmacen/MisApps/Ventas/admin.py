from django.contrib import admin
from MisApps.Ventas.models import Venta
from MisApps.Ventas.models import VentaProducto

# Register your models here.
admin.site.register (Venta)
admin.site.register (VentaProducto)