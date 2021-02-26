from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    score = serializers.IntegerField(min_value=1, max_value=10, required=True)

    class Meta:
        model = Review
        exclude = ['title']

    def validate(self, attrs):
        title_id = self.context.get('title_id')
        author_id = self.context.get('author_id')
        request_method = self.context.get('method')
        if not request_method:
            if Review.objects.filter(title__id=title_id,
                                     author__id=author_id).exists():
                raise serializers.ValidationError(
                    'only 1 review per title is allowed'
                )
        return attrs
