from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from api.v1.views import (CategoryViewSet, GenreViewSet, TitleViewSet,
                          UserViewSet, SignupView)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register('categories', CategoryViewSet, basename='category')
router.register('genres', GenreViewSet, basename='genre')
router.register('titles', TitleViewSet, basename='title')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='create_token'),
    path('auth/signup/', SignupView.as_view(), name='signup'),
]
