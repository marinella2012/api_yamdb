from rest_framework import serializers
from statistics import mean
from django.shortcuts import get_object_or_404

from ..models import Genre, Title
from .category_serializer import CategorySerializer
from .genre_serializer import GenreSerializer


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.CategorySerializer()
    rating = serializers.SerializerMethodField()
    genre = serializers.GenreSerializer(many=True)

    class Meta:
        model = Title
        fields = '__all__'

    def get_rating(self, obj):
        scores_list = obj.reviews.all().values_list('score', flat=True)
        return mean(scores_list)

    def create(self, validated_data):
        genres_data = validated_data.pop('genre')
        title = Title.objects.create(**validated_data)
        for genre_data in genres_data:
            genre = get_object_or_404(Genre, slug=genre_data)
            title.genre_set.add(genre)
