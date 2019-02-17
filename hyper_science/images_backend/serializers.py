from rest_framework import serializers

from images_backend import *


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instrument
        fields = '__all__'


class DetectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Detector
        fields = '__all__'


class AcquisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Acquisition
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '__all__'


class AlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Algorithm
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Classification
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class AttributeDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AttributeDefinition
        fields = '__all__'


class InstanceValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InstanceValue
        fields = '__all__'
