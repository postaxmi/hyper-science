from django_filters import rest_framework as filters

from images_backend import models

# https://django-filter.readthedocs.io/en/master/guide/rest_framework.html


class CategoryDefinitionFilter(filters.FilterSet):
    class Meta:
        model = models.CategoryDefinition

        fields = {
            'name': ['exact', 'contains', 'icontains'],
            'uuid': ['exact'],
            'parent': ['exact'],
        }


class CategoryDictionaryFilter(filters.FilterSet):
    class Meta:
        model = models.CategoryDictionary

        fields = {
            'uuid': ['exact'],
            'category__uuid': ['exact'],
            'attribute__uuid': ['exact'],
        }
