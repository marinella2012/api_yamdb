from rest_framework import filters, mixins, viewsets

from users.permissions import IsAdministratorOrReadOnly

from ..models.category import Category
from ..serializers.category_serializer import CategorySerializer


class CreateListViewDelSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoryViewSet(CreateListViewDelSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdministratorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'
