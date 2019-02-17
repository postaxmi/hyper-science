
from rest_framework import viewsets
from images_backend import  serializers
from images_backend import models
from url_filter.filtersets import ModelFilterSet
from rest_framework import generics

class RetrieveUpdateDestroyAPIPersonView(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Person.objects.all()
    serializer_class=serializers.PersonSerializer

class ListCreateAPIPersonView(generics.ListCreateAPIView):
    queryset=models.Person.objects.all()
    serializer_class=serializers.PersonSerializer