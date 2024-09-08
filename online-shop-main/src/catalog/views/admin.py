from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from catalog.models import Category
from catalog.serializers import admin as adm_srz


class CategoryViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(depth=1)
        else:
            return Category.objects.all()

    def  get_serializer_class(self):
        match self.action:
            case 'list':
                return adm_srz.CategoryTreeSerializer
            case 'create':
                return adm_srz.CreateCategoryNodeSerializer
            case 'retrieve':
                return adm_srz.CategoryNodeSerializer
            case 'update':
                return adm_srz.CategoryModificationSerializer
            case 'partial_update':
                return adm_srz.CategoryModificationSerializer
            case 'destroy':
                return adm_srz.CategoryModificationSerializer
            case _:
                raise NotAcceptable()
