from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions

from ..models.review import Review
from ..serializers.comment_serializer import CommentSerializer
from users.permissions import IsAuthorOrReadOnly, IsAdministrator, IsModerator


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly
                          | IsAuthorOrReadOnly
                          | IsModerator
                          | IsAdministrator]

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

    # def update(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
