from rest_framework import viewsets

<<<<<<< HEAD
from ..models.title import Title
from ..serializers.title_serializer import TitleSerializer
=======
from users.permissions import IsAdministratorOrReadOnly
from ..filters import TitleFilter
from ..models.title import Title
from ..serializers.title_serializer import (TitleViewSerializer,
                                            TitleCreateSerializer)
>>>>>>> master


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
<<<<<<< HEAD
    serializer_class = TitleSerializer
    permission_classes = []
    filter_backends = []
    #
    # def get_serializer_class(self):
    #     if self.action in ('create', 'partial_update'):
    #         return TitleSlugSerializer
    #     return TitleSerializer
=======
    permission_classes = [IsAdministratorOrReadOnly]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return TitleViewSerializer
        return TitleCreateSerializer
>>>>>>> master
