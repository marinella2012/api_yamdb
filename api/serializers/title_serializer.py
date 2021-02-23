from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db.models import Avg

from ..models.category import Category
from ..models.genre import Genre
from ..models.title import Title
from .category_serializer import CategorySerializer
from .genre_serializer import GenreSerializer


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer()
    rating = serializers.SerializerMethodField(allow_null=True)

    class Meta:
        model = Title
        fields = '__all__'

    def get_rating(self, obj):
        return obj.reviews.aggregate(Avg('score'))

    def to_internal_value(self, data):
        genre_slug_list = data.get('genre')
        category_slug = data.get('category')
        return {'name': data.get('name'),
                'year': data.get('year'),
                'description': data.get('description'),
                'genre': genre_slug_list,
                'category': category_slug}

    def create(self, validated_data):
        category = get_object_or_404(Category,
                                     slug=validated_data.get('category'))
        title = Title.objects.create(
            category=category,
            name=validated_data.get('name'),
            year=validated_data.get('year'),
            description=validated_data.get('description')
        )
        genres = Genre.objects.filter(slug__in=validated_data.get('genre'))
        for genre in genres:
            title.genre_set.add(genre)
        title.save()
        return title
