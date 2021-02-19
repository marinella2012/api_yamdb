from rest_framework import viewsets

from ..serializers import TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    permission_classes = []
