from rest_framework import viewsets

from ..models.title import Title
from ..serializers.title_serializer import TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = []
    filter_backends = []
    #
    # def get_serializer_class(self):
    #     if self.action in ('create', 'partial_update'):
    #         return TitleSlugSerializer
    #     return TitleSerializer
