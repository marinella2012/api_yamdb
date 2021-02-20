from rest_framework import mixins, viewsets


class RetrieveUpdateViewSet(viewsets.GenericViewSet,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin):
    pass
