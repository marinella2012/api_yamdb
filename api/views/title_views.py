from django.db.models import Avg
from rest_framework import viewsets

from users.permissions import IsAdministratorOrReadOnly
from ..filters import TitleFilter
from ..models.title import Title
from ..serializers.title_serializer import (TitleCreateSerializer,
                                            TitleViewSerializer)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    permission_classes = [IsAdministratorOrReadOnly]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return TitleViewSerializer
        return TitleCreateSerializer
