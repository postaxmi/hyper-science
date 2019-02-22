from django_filters import rest_framework as filters

from images_backend import models

# https://django-filter.readthedocs.io/en/master/guide/rest_framework.html


class CategoryDefinitionFilter(filters.FilterSet):
    class Meta:
        model = models.CategoryDefinition

        fields = {
            'name': ['exact', 'iexact', 'contains', 'icontains'],
            'uuid': ['exact', 'iexact', 'contains', 'icontains'],
            'parent__uuid': ['exact', 'iexact', 'contains', 'icontains'],
        }


class CategoryDictionaryFilter(filters.FilterSet):
    class Meta:
        model = models.CategoryDictionary

        fields = {
            'uuid': ['exact', 'iexact', 'contains', 'icontains'],
            'category__uuid': ['exact', 'iexact', 'contains', 'icontains'],
            'category__name': ['exact', 'iexact', 'contains', 'icontains'],
            'category__parent__uuid': ['exact', 'iexact', 'contains', 'icontains'],
            'attribute__uuid': ['exact', 'iexact', 'contains', 'icontains'],
            'attribute__name': ['exact', 'iexact', 'contains', 'icontains'],
            'attribute__description': ['exact', 'iexact', 'contains', 'icontains'],
            'attribute__value_type': ['exact', 'iexact'],
        }
