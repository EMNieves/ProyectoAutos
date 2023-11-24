from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MisApps.ventas.models import Ventas

class VentasSerializer(serializers.ModelSerializer):
    # len_nombreCliente = serializers.SerializerMethodField()
    class Meta:
        model = Ventas
        fields = "__all__"