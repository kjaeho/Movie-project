from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import UserSerializer
from movies.serializers import MovieSerializer

from .models import User
from movies.models import Movie,Rating

from .forms import CustomUserChangeForm

# Create your views here.
User = get_user_model()


@api_view(['GET'])
def userdetail(request):
    user = request.user
    rated_movies = Rating.objects.filter(user_id=user).exclude(star=-1).values('movie_id')
    liked_movies = Rating.objects.filter(user_id=user,star=-1).values('movie_id')

    rated_movie_list = Movie.objects.filter(movie_id__in=rated_movies)
    liked_movie_list = Movie.objects.filter(movie_id__in=liked_movies)

    rated_movie_data = MovieSerializer(rated_movie_list,many=True)
    liked_movie_data = MovieSerializer(liked_movie_list,many=True)
    
    user_data = get_object_or_404(User,email=user)
    user_serializer=UserSerializer(user_data)

    rcnt = Rating.objects.filter(user=user).exclude(star=-1).count()
    lcnt = Rating.objects.filter(user=user,star=-1).count()
    return Response({
        'rated_movie_data':rated_movie_data.data,
        'liked_movie_data':liked_movie_data.data,
        'user_data':user_serializer.data,
        'rated_movie_cnt':rcnt,
        'liked_movie_cnt':lcnt,
    })
    return Response()

@api_view(['GET'])
def user_rating_check(request):
    user=request.user
    rating_cnt = Rating.objects.filter(user_id=user).count()
    check=False
    if rating_cnt>=10:
        check=True
    return Response(check)

@api_view(['POST'])
def updateUser(request, useremail):
    selected_user = get_object_or_404(User,email=useremail)
    serializer=UserSerializer(data=request.data,instance=selected_user)
    if serializer.is_valid(raise_exception=True):
        serializer.save(email=useremail)
        return Response()