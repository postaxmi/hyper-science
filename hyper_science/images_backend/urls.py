from django.urls import path, re_path

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
    re_path(
        r'persons/(?P<pk>[\w\d]{32})/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Person.objects.all(), serializer_class=serializers.PersonSerializer),
        name='person-update'),
    path(
        'instruments/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Instrument.objects.all(),
            serializer_class=serializers.InstrumentSerializer),
        name='instrument-list'),
    re_path(
        r'instruments/(?P<pk>[\w\d]{32})/',
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
    re_path(
        r'detectors/(?P<pk>[\w\d]{32})/',
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
    re_path(
        r'acquisitions/(?P<pk>[\w\d]{32})/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Acquisition.objects.all(),
            serializer_class=serializers.AcquisitionSerializer),
        name='acquisition-update'),
    path(
        'images/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Image.objects.all(), serializer_class=serializers.ImageSerializer),
        name='image-list'),
    re_path(
        r'images/(?P<pk>[\w\d]{32})/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Image.objects.all(), serializer_class=serializers.ImageSerializer),
        name='image-update'),
    path(
        'algorithms/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Algorithm.objects.all(),
            serializer_class=serializers.AlgorithmSerializer),
        name='algorithm-list'),
    re_path(
        r'algorithms/(?P<pk>[\w\d]{32})/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Algorithm.objects.all(),
            serializer_class=serializers.AlgorithmSerializer),
        name='algorithm-update'),
    path(
        'articles/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Article.objects.all(), serializer_class=serializers.ArticleSerializer),
        name='article-list'),
    re_path(
        r'articles/(?P<pk>[\w\d]{32})/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Article.objects.all(), serializer_class=serializers.ArticleSerializer),
        name='article-update'),
    path(
        'classifications/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Classification.objects.all(),
            serializer_class=serializers.ClassificationSerializer),
        name='classification-list'),
    re_path(
        r'classifications/(?P<pk>[\w\d]{32})/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Classification.objects.all(),
            serializer_class=serializers.ClassificationSerializer),
        name='classification-update'),
    path(
        'categories/',
        generics.ListCreateAPIView.as_view(
            queryset=models.Category.objects.all(),
            serializer_class=serializers.CategorySerializer),
        name='category-list'),
    re_path(
        r'categories/(?P<pk>[\w\d]{32})/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.Category.objects.all(),
            serializer_class=serializers.DeepCategorySerializer),
        name='category-update'),
    path(
        'attributes/',
        generics.ListCreateAPIView.as_view(
            queryset=models.AttributeDefinition.objects.all(),
            serializer_class=serializers.AttributeDefinitionSerializer),
        name='attribute-list'),
    re_path(
        r'attributes/(?P<pk>[\w\d]{32})/',
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
    re_path(
        r'instances/(?P<pk>[\w\d]{32})/',
        generics.RetrieveUpdateDestroyAPIView.as_view(
            queryset=models.InstanceValue.objects.all(),
            serializer_class=serializers.InstanceValueSerializer),
        name='article-update'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'xml', 'html'])
