from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from movieApi.views import MovieViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]