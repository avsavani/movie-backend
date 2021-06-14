from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import viewsets,status
from django.contrib.auth.models import User
from .models import Movie,Rating
from .serializers import MovieSerializer,RatingSerializer,UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(methods=['POST'], detail=True)
    def rate_movie(self, request, pk=None):
        if  'stars' in request.data:
            user = request.user
            print('User:',user)
            movie =  Movie.objects.get(id=pk)
            stars = request.data['stars']

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                message = { 'message':'Rating has been updated'}
                print(message['message'])
                return Response(message, status=status.HTTP_200_OK)
            except:
                Rating.objects.create(user = user, movie=movie, stars=stars)
                message = { 'message':'The rating has been created'}
                print(message['message'])
                return Response(message, status=status.HTTP_200_OK)

            message = { 'message':'Its not workin'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'message':'Please Enter the stars'}, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {'message':'you cant update ratings like that'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        response = {'message':'you cant update ratings like that'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)