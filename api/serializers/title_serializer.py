from django.db.models import Avg
from rest_framework import serializers

from .category_serializer import CategorySerializer
from .genre_serializer import GenreSerializer
from ..models.category import Category
from ..models.genre import Genre
from ..models.title import Title


class TitleViewSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField(allow_null=True)

    class Meta:
        model = Title
        fields = '__all__'

    def get_rating(self, obj):
        if obj.reviews.all().exists():
            return obj.reviews.all().aggregate(Avg('score'))['score__avg']
        return None


class TitleCreateSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(slug_field='slug',
                                         many=True,
                                         queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all())

    class Meta:
        model = Title
        fields = '__all__'
