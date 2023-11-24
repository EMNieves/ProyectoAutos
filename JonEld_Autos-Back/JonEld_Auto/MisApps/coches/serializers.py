from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MisApps.coches.models import Coches

class CochesSerializer(serializers.ModelSerializer):
    # len_nombreCliente = serializers.SerializerMethodField()
    class Meta:
        model = Coches
        fields = "__all__"
        