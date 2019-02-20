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


class CategoryDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryDefinition
        fields = '__all__'


class DeepCategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = models.CategoryDefinition
        fields = '__all__'

    def get_children(self, obj):
        return [DeepCategorySerializer().to_representation(cat) for cat in obj.children.all()]


class AttributeDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AttributeDefinition
        fields = '__all__'


class InstanceValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InstanceValue
        fields = '__all__'
