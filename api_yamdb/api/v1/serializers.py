from rest_framework import serializers
from reviews.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор модели Category."""

    class Meta:
        # fields = ()
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор модели Genre."""

    class Meta:
        # fields = ()
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор модели Title."""

    class Meta:
        # fields = ()
        model = Title
