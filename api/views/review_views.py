from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets

from users.permissions import IsAuthorOrModerOrAdminOrReadOnly
from ..models.title import Title
from ..serializers.review_serializer import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrModerOrAdminOrReadOnly]

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user,
                            title=title)

    def get_serializer_context(self):
        context = super(ReviewViewSet, self).get_serializer_context()
        context.update({
            'title_id': self.kwargs.get('title_id'),
            'author_id': self.request.user.id
        })
        if self.request.method == 'PATCH':
            context.update({'method': 'patch'})
        return context
