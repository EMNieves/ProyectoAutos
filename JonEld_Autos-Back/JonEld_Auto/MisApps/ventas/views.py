from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status

from MisApps.ventas.models import Ventas
from MisApps.ventas.serializers import VentasSerializer

# Create your views here.


class VentasList(generics.ListCreateAPIView):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer



class VentasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer