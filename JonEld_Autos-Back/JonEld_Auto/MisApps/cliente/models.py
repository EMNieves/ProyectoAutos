from django.db import models

# Create your models here.


class Cliente(models.Model):
    nit_cCliente = models.CharField(max_length=100)
    nombreCliente = models.CharField(max_length=100)
    apellidoCliente = models.CharField(max_length=100)
    telefonoCliente = models.CharField(max_length=12)
    direccionCliente = models.CharField(max_length=100)
    correoCliente = models.EmailField(max_length=100)
    ciudadCliente = models.CharField(max_length=100)
    passwordCliente = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreCliente

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
