from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status

from MisApps.marcas.models import Marcas
from MisApps.marcas.serializers import MarcasSerializer

# Create your views here.


class MarcasList(generics.ListCreateAPIView):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializer



class MarcasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializer