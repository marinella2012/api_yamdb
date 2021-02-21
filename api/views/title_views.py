from rest_framework import viewsets

from ..serializers.title_serializer import TitleSerializer
from ..models import Title


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

