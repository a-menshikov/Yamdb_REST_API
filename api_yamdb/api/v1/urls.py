from django.urls import include, path
from rest_framework import routers

from api.v1.views import CategoryViewSet, GenreViewSet, TitleViewSet

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet, basename='category')
router.register('genres', GenreViewSet, basename='genre')
router.register('titles', TitleViewSet, basename='title')

urlpatterns = [
    path('', include(router.urls)),
    
]
