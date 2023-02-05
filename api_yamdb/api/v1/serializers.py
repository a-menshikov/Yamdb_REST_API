import re

from rest_framework import serializers
from django.utils import timezone
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.shortcuts import get_object_or_404


from reviews.models import Category, Genre, Title
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели User."""

    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name',
                  'bio', 'role')
        model = User


class UsersMeSerializer(serializers.ModelSerializer):
    """Сериализатор для эндпоинта users/me/."""

    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name',
                  'bio')
        model = User


class YamdbTokenObtainPairSerializer(TokenObtainPairSerializer):
    confirmation_code = serializers.CharField(required=True)

    def validate(self, attrs):
        data = super().validate(attrs)
        return {'access': data['access']}

    def validate_username(self, value):
        return get_object_or_404(User, username=value)


class SignupSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователей."""

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'me нельзя использовать в качестве имени'
            )
        return value

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
        lookup_field = 'slug'


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
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    """Базовый сериализатор модели Title."""
    rating = serializers.IntegerField(read_only=True)

    def validate_year(self, value):
        """Проверка года на будущее время."""
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError(
                'Марти, ты опять взял Делориан без спроса?!'
            )
        return value

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')


class TitleReadSerializer(TitleSerializer):
    """Сериализатор модели Title для чтения."""
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)


class TitleWriteSerializer(TitleSerializer):
    """Сериализатор модели Title для записи."""
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
        required=False
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )
