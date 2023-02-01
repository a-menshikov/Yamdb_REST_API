from api.v1.serializers import (CategorySerializer, GenreSerializer,
                                TitleSerializer)
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Category."""

    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Genre."""

    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Title."""

    serializer_class = TitleSerializer
