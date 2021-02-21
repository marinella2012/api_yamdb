from rest_framework import filters, status, viewsets
from rest_framework.response import Response

from ..models import Genre
from ..serializers import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = []

    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)

    def retrieve(self):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
