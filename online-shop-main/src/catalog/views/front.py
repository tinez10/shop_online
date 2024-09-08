from rest_framework import viewsets
from catalog.models import Category
from catalog.serializers.front import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.public()
    serializer_class = CategorySerializer