
from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models.category import Category
from ..serializers.category_serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

    search_fields = ('name',)

    def retrieve(self):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
