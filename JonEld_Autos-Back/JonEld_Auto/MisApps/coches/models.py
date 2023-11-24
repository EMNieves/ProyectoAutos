from django.db import models
from MisApps.cliente.models import Cliente
from MisApps.marcas.models import Marcas

# Create your models here.


class Coches(models.Model):
    matricula = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="cliente_id")
    marcas_id = models.ForeignKey(Marcas, on_delete=models.CASCADE, verbose_name="marcas_id")

    def __str__(self):
        return self.matricula

    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"