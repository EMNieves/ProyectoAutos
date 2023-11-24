from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status

from MisApps.coches.models import Coches
from MisApps.coches.serializers import CochesSerializer

# Create your views here.


class CochesList(generics.ListCreateAPIView):
    queryset = Coches.objects.all()
    serializer_class = CochesSerializer



class CochesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coches.objects.all()
    serializer_class = CochesSerializer