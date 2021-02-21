from rest_framework import viewsets

from ..serializers.title_serializer import TitleSerializer, TitleSlugSerializer
from ..models import Title


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    permission_classes = []
    filter_backends = []

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return TitleSlugSerializer
        return TitleSerializer

    def get_queryset(self):
        return Title.objects.annotate(rating=Avg('reviews__score'))
