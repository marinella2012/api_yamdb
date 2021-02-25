<<<<<<< HEAD
from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models.genre import Genre
from ..serializers.genre_serializer import GenreSerializer
from users.permissions import IsAdministrator


class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdministrator | IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['=slug', 'name']
    lookup_field = 'slug'
=======
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
>>>>>>> master
