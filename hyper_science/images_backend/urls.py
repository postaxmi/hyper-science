from django.urls import path

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework import generics
from rest_framework.urlpatterns import format_suffix_patterns

from images_backend import views, models, serializers

router = DefaultRouter()

urlpatterns = [
    path(
        'persons/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Person.objects.all(), serializer_class=serializers.PersonSerializer),
        name='person-list'),
    path(
        'persons/<uuid:pk>/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Person.objects.all(), serializer_class=serializers.PersonSerializer),
        name='person-update'),
    path(
        'instruments/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Instrument.objects.all(),
            serializer_class=serializers.InstrumentSerializer),
        name='instrument-list'),
    path(
        'instruments/<uuid:pk>/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Instrument.objects.all(),
            serializer_class=serializers.InstrumentSerializer),
        name='instrument-update'),
    path(
        'detectors/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Detector.objects.all(),
            serializer_class=serializers.DetectorSerializer),
        name='detector-list'),
    path(
        'detectors/<uuid:pk>/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Detector.objects.all(),
            serializer_class=serializers.DetectorSerializer),
        name='detector-update'),
    path(
        'acquisitions/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Acquisition.objects.all(),
            serializer_class=serializers.AcquisitionSerializer),
        name='acquisition-list'),
    path(
        'acquisitions/<uuid:pk>/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Acquisition.objects.all(),
            serializer_class=serializers.AcquisitionSerializer),
        name='acquisition-update'),
    path(
        'images/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Image.objects.all(), serializer_class=serializers.ImageSerializer),
        name='image-list'),
    path(
        'images/<uuid:pk>/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Image.objects.all(), serializer_class=serializers.ImageSerializer),
        name='image-update'),
    path(
        'algorithms/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Algorithm.objects.all(),
            serializer_class=serializers.AlgorithmSerializer),
        name='algorithm-list'),
    path(
        'algorithms/<uuid:pk>/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Algorithm.objects.all(),
            serializer_class=serializers.AlgorithmSerializer),
        name='algorithm-update'),
    path(
        'articles/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Article.objects.all(), serializer_class=serializers.ArticleSerializer),
        name='article-list'),
    path(
        'articles/<uuid:pk>/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Article.objects.all(), serializer_class=serializers.ArticleSerializer),
        name='article-update'),
    path(
        'classifications/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Classification.objects.all(),
            serializer_class=serializers.ClassificationSerializer),
        name='classification-list'),
    path(
        'classifications/<uuid:pk>/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Classification.objects.all(),
            serializer_class=serializers.ClassificationSerializer),
        name='classification-update'),
    path(
        'categorys/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Category.objects.all(),
            serializer_class=serializers.CategorySerializer),
        name='category-list'),
    path(
        'categorys/<uuid:pk>/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Category.objects.all(),
            serializer_class=serializers.CategorySerializer),
        name='category-update'),
    path(
        'attributes/',
        generics.ListCreateAPIView.as_view(
            queryset=models.AttributeDefinition.objects.all(),
            serializer_class=serializers.AttributeDefinitionSerializer),
        name='attribute-list'),
    path(
        'attributes/<uuid:pk>/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.AttributeDefinition.objects.all(),
            serializer_class=serializers.AttributeDefinitionSerializer),
        name='attribute-update'),
    path(
        'instances/',
        generics.ListCreateAPIView.as_view(
            queryset=models.InstanceValue.objects.all(),
            serializer_class=serializers.InstanceValueSerializer),
        name='instance-list'),
    path(
        'instances/<uuid:pk>/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.InstanceValue.objects.all(),
            serializer_class=serializers.InstanceValueSerializer),
        name='article-update'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'xml', 'html'])
