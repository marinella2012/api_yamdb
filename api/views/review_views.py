from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions

from ..models.title import Title
from ..serializers.review_serializer import ReviewSerializer
from users.permissions import (IsAuthorOrReadOnly,
                               IsAdministratorOrReadOnly,
                               IsModerator)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly
                          | IsAuthorOrReadOnly
                          | IsAdministratorOrReadOnly
                          | IsModerator]

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
        return context
