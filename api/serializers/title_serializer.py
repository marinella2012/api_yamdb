from rest_framework import serializers
import statistics

from ..models.category import Category
from ..models.genre import Genre
from ..models.title import Title
from .genre_serializer import GenreSerializer
from .category_serializer import CategorySerializer


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
        return None

    def to_internal_value(self, data):
        try:
            genre_slug_list = data.get('genre')
            name = data['name']
            return {'name': name,
                    'year': data.get('year'),
                    'description': data.get('description'),
                    'genre': genre_slug_list,
                    'category': data.get('category')}
        except KeyError:
            raise serializers.ValidationError({'name': 'field is required'},
                                              code='invalid')

    def create(self, validated_data):
        if Category.objects.filter(
                slug=validated_data.get('category')
        ).exists():
            category = Category.objects.get(
                slug=validated_data.get('category')
            )
            title = Title.objects.create(
                category=category,
                name=validated_data.get('name'),
                year=validated_data.get('year'),
                description=validated_data.get('description')
            )
        else:
            title = Title.objects.create(
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
