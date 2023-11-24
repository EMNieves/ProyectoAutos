from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MisApps.marcas.models import Marcas

class MarcasSerializer(serializers.ModelSerializer):
    # len_nombreCliente = serializers.SerializerMethodField()
    class Meta:
        model = Marcas
        fields = "__all__"
        