from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from ..serializers.title_serializer import TitleSerializer
from ..models.title import Title
from ..models.category import Category
from users.permissions import IsAdministratorOrReadOnly


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = [IsAdministratorOrReadOnly]
    serializer_class = TitleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'genre', 'name', 'year']

    # def update(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def perform_update(self, serializer):
        category_slug = self.request.data['category']
        if Category.objects.filter(slug=category_slug).exists():
            category = Category.objects.get(slug=category_slug)
            serializer.save(category__slug=category_slug)
