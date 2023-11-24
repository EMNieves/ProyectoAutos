from django.db import models
from MisApps.cliente.models import Cliente
from MisApps.coches.models import Coches

# Create your models here.


class Ventas(models.Model):
    precioVenta = models.CharField(max_length=100)
    metodoPago = models.CharField(max_length=100)
    fechaVenta = models.DateField(max_length=100)
    telefonoCliente = models.CharField(max_length=12)
    direccionCliente = models.CharField(max_length=100)
    correoCliente = models.EmailField(max_length=100)
    ciudadCliente = models.CharField(max_length=100)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="cliente_id")
    coches_id = models.ForeignKey(Coches, on_delete=models.CASCADE, verbose_name="coches_id")

    def __str__(self):
        return self.precioVenta

    class Meta:
        verbose_name = "venta"
        verbose_name_plural = "ventas"