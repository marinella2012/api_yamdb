from rest_framework import serializers

from ..models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    review = serializers.ModelField(read_only=True,
                                    model_field='review')

    class Meta:
        model = Comment
        exclude = ['review']
