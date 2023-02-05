from django.urls import include, path
from rest_framework import routers

from api.v1.views import (CategoryViewSet, GenreViewSet, TitleViewSet,
                          UserViewSet, SignupView, YamdbTokenObtainPairView,
                          UsersMeView, CommentViewSet, ReviewViewSet)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register('categories', CategoryViewSet, basename='category')
router.register('genres', GenreViewSet, basename='genre')
router.register('titles', TitleViewSet, basename='title')
router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='review',
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment',
)


urlpatterns = [
    path('auth/token/', YamdbTokenObtainPairView.as_view(),
         name='create_token'),
    path('auth/signup/', SignupView.as_view(), name='signup'),
    path('users/me/', UsersMeView.as_view(), name='me'),
    path('', include(router.urls)),
]
