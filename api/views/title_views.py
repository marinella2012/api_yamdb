from django.db.models import Avg
from rest_framework import viewsets
from rest_framework.response import Response

from users.permissions import IsAdministratorOrReadOnly

from ..filters import TitleFilter
from ..models.title import Title
from ..serializers.title_serializer import (TitleCreateSerializer,
                                            TitleViewSerializer)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = [IsAdministratorOrReadOnly]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return TitleViewSerializer
        return TitleCreateSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        rating = instance.reviews.all().aggregate(Avg('score'))['score__avg']
        data = self.get_serializer(instance).data
        data['rating'] = rating
        return Response(data)
