from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MisApps.Clientes.models import Clientes

class ClienteSerializer(serializers.ModelSerializer):
    # len_nombreCliente = serializers.SerializerMethodField()
    class Meta:
        model = Clientes
        fields = "__all__"