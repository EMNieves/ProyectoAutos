from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status

from MisApps.Clientes.models import Clientes
from MisApps.Clientes.serializers import ClienteSerializer

# Create your views here


class ClientesList(generics.ListCreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer



class ClientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer
