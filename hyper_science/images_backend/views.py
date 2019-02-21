from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from images_backend import models, serializers, filters


# If we were to apply the DeepCategorySerializer also to the list view, we would see the tree and
# all the children repeated again.
class CategoryDefinitionListCreateAPI(ListCreateAPIView):
    queryset = models.CategoryDefinition.objects.all()
    serializer_class = serializers.CategoryDefinitionSerializer
    filterset_class = filters.CategoryDefinitionFilter
