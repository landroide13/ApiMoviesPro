from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import CommentMovie, CustomerProfile, Movie, Rating
from .serializer import CommentSerializer, CustomerSerializer, MovieSerializer, RatingSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication, )
    #permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:

            movie = Movie.objects.get(id=pk)

            stars = request.data['stars']
            user = request.user
            #user = User.objects.get(id=1)
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()

                serializer = RatingSerializer(rating, many=False)    
                response = {'message': 'Rating Updated..', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)

                serializer = RatingSerializer(rating, many=False)    
                response = {'message': 'Rating Created..', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)    
        else:
            response = {'message': 'Please provived starts'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def comment_movie(self, request, pk=None):
        if 'comments' in request.data:

            movie = Movie.objects.get(id=pk)

            comments = request.data['comments']
            user = request.user
            #user = User.objects.get(id=1)
            try:
                comment = CommentMovie.objects.get(user=user.id, movie=movie.id)
                comment.comments = comments
                comment.save()

                serializer = CommentSerializer(comment, many=False)    
                response = {'message': 'Comment Updated..', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                comment = CommentMovie.objects.create(user=user, movie=movie, stars=stars)

                serializer = CommentSerializer(comment, many=False)    
                response = {'message': 'Comment Created..', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)    
        else:
            response = {'message': 'Please provived Comment'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)




class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerSerializer
    #authentication_classes = (TokenAuthentication, )
    #permission_classes = (IsAuthenticated,)












