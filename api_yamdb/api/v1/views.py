from rest_framework import viewsets

# from reviews.models import Category, Genre, Title
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Category."""

    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Genre."""

    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Title."""

    serializer_class = TitleSerializer
