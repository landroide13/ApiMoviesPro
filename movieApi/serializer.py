from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Movie, Rating, CustomerProfile
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'num_stars', 'avg_rating')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'movie')    

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ( 'id', 'birth_date')










