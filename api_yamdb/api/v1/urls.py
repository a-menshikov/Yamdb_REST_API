from django.urls import path, include
from rest_framework import routers

from api.v1.views import (CategoryViewSet, GenreViewSet, TitleViewSet,
                          UserViewSet, SignupView, YamdbTokenObtainPairView,
                          UsersMeView)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register('categories', CategoryViewSet, basename='category')
router.register('genres', GenreViewSet, basename='genre')
router.register('titles', TitleViewSet, basename='title')


urlpatterns = [
    path('auth/token/', YamdbTokenObtainPairView.as_view(), name='create_token'),
    path('auth/signup/', SignupView.as_view(), name='signup'),
    path('users/me/', UsersMeView.as_view(), name='me'),
    path('', include(router.urls)),
]
