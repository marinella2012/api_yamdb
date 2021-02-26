from rest_framework import filters

from users.permissions import IsAdministratorOrReadOnly
from .genre_views import CreateListViewDelSet
from ..models.category import Category
from ..serializers.category_serializer import CategorySerializer


class CategoryViewSet(CreateListViewDelSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdministratorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'
