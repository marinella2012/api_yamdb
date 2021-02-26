from rest_framework import filters, viewsets, mixins

from users.permissions import IsAdministratorOrReadOnly
from ..models.genre import Genre
from ..serializers.genre_serializer import GenreSerializer


class GenreViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdministratorOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
