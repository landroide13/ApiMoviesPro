from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from movieApi.views import CustomerViewSet, MovieViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)
router.register('customers', CustomerViewSet)


urlpatterns = [
    path('', include(router.urls)),
]