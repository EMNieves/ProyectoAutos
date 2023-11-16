from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status

from MisApps.Ventas.models import Venta
from MisApps.Ventas.serializers import VentaSerializer
# Create your views here.

class VentasList(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer



class VentasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
