from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions

from users.permissions import IsAuthorOrModerOrAdminOrReadOnly
from ..models.review import Review
from ..serializers.comment_serializer import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrModerOrAdminOrReadOnly]

    def get_queryset(self):
        review = get_object_or_404(Review,
                                   title__id=self.kwargs.get('title_id'),
                                   id=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review,
                                   title__id=self.kwargs.get('title_id'),
                                   id=self.kwargs.get('review_id'))
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user,
                            review=review)
