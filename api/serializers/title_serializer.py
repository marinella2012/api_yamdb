from rest_framework import serializers
from django.shortcuts import get_object_or_404
import statistics

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
        if obj.reviews.all().exists():
            scores = obj.reviews.all().values_list('score', flat=True)
            avg = statistics.fmean(scores)
            return avg
        return 'None'

    def to_internal_value(self, data):
        genre_slug_list = data.get('genre')
        category_slug = data.get('category')
        if not data.get('name'):
            raise serializers.ValidationError('name is required')
        return {'name': data.get('name'),
                'year': data.get('year'),
                'description': data.get('description'),
                'genre': genre_slug_list,
                'category': category_slug}

    def create(self, validated_data):
        category_slug = validated_data.get('category')
        category = None
        if Category.objects.filter(slug=category_slug).exists():
            category = Category.objects.get(slug=category_slug)
        title = Title.objects.create(
            category=category,
            name=validated_data.get('name'),
            year=validated_data.get('year'),
            description=validated_data.get('description')
        )
        slugs = validated_data.get('genre')
        if slugs:
            for slug in slugs:
                if Genre.objects.filter(slug=slug).exists():
                    genre = Genre.objects.get(slug=slug)
                    title.genre.add(genre)
                continue
        title.save()
        return title
