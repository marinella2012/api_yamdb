from rest_framework import filters, status, viewsets
from rest_framework.response import Response

from ..models import Genre
from ..serializers import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    lookup_field = 'slug'
    serializer_class = GenreSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
