from rest_framework import filters, mixins, viewsets

from users.permissions import IsAdministratorOrReadOnly

from ..models.genre import Genre
from ..serializers.genre_serializer import GenreSerializer


class CreateListViewDelSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class GenreViewSet(CreateListViewDelSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdministratorOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
