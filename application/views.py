from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import HttpRequest , JsonResponse
from rest_framework import generics

# Create your views here.
class create_data(generics.CreateAPIView):
    queryset=data.objects.all()
    serializer_class=dataSerializer

class read_data(generics.ListAPIView):
    queryset=data.objects.all()
    serializer_class=dataSerializer

class update_data(generics.RetrieveUpdateAPIView):
    queryset=data.objects.all()
    serializer_class=dataSerializer

class delete_data(generics.DestroyAPIView):
    queryset=data.objects.all()
    serializer_class=dataSerializer