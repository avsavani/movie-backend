from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, RatingViewSet, UserViewSet

router = DefaultRouter()
router.register('movies',MovieViewSet)
router.register('ratings',RatingViewSet)
router.register('users',UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
