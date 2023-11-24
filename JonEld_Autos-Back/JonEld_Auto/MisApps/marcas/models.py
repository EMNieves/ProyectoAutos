from django.db import models

# Create your models here.


class Marcas(models.Model):
    codigo_m = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo_m

    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"