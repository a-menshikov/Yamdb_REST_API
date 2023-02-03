import re

from rest_framework import serializers
from django.utils import timezone

from reviews.models import Category, Genre, Title
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели User."""

    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name',
                  'bio', 'role')
        model = User


class SignupSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователей."""

    class Meta:
        fields = ('username', 'email')
        model = User


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор модели Category."""

    def validate_slug(self, value):
        """Проверка соответствия слага категории."""
        if not re.fullmatch(r'^[-a-zA-Z0-9_]+$', value):
            raise serializers.ValidationError(
                'Псевдоним категории не соотвествует формату'
            )
        return value

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор модели Genre."""

    def validate_slug(self, value):
        """Проверка соответствия слага жанра."""
        if not re.fullmatch(r'^[-a-zA-Z0-9_]+$', value):
            raise serializers.ValidationError(
                'Псевдоним жанра не соотвествует формату'
            )
        return value

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор модели Title."""

    def validate_year(self, value):
        """Проверка года на будущее время."""
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError(
                'Марти, ты опять взял Делориан без спроса?!'
            )
        return value

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title
