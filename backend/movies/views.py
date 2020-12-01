from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Movie, Genre, Actor, Keyword, Rating
from .serializers import MovieSerializer, GenreSerializer, ActorSerializer, KeywordSerializer, RatingSerializer

from django.db.models import Sum,Avg,Count,Max,Q

from django.core.exceptions import ObjectDoesNotExist

import random

import pandas as pd
import numpy as np

import pymysql
from sqlalchemy import create_engine
from sklearn.metrics.pairwise import cosine_similarity


# Create your views here.

@api_view(['GET'])
def recentList(request,page_num,flag):
    if flag:
        movies = Movie.objects.order_by('-releasedate')
    else:
        movies = Movie.objects.filter(rcnt__gte=1000).order_by('-ravg')
    paginator = Paginator(movies,12)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = MovieSerializer(page_obj, many=True)
    return Response({
        'movieData':serializer.data,
        'pageNum':movies.count()//12
        })

@api_view(['GET'])
def listByCategory(request,genre,nation,year,page_num,sort):
    flag=False
    if nation=="0" or nation=="해외":
        if nation=="해외":
            flag=True
        nation=""
    if year=="0":
        year=""
    if genre=="0":
        genre=False
    if genre:
        if genre=="로맨스":
            genre="멜로/로맨스"
        movies =  Movie.objects.filter(genres=genre,nation__icontains=nation,releasedate__icontains=year)
    else:
        movies = Movie.objects.filter(nation__icontains=nation, releasedate__icontains=year)

    if flag:
        movies=movies.exclude(nation__icontains="한국")

    if movies.count()%12:
        page_cnt=movies.count()//12+1
    else:
        page_cnt=movies.count()//12

    if sort:
        movies=movies.order_by('-releasedate')
    else:
        movies=movies.order_by('-ravg')

    paginator = Paginator(movies,12)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = MovieSerializer(page_obj, many=True)

    return Response({
        'movieData':serializer.data,
        'pageNum':page_cnt
    })

@api_view(['GET'])
def listByGenre(request,genre,page_num):
    if genre == '로맨스':
        genre = '멜로/로맨스'
    movies = Movie.objects.filter(genres=genre)
    paginator = Paginator(movies,12)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = MovieSerializer(page_obj, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def listByActor(request,actor,page_num):
    movies = Movie.objects.filter(actors=actor)
    paginator = Paginator(movies,12)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = MovieSerializer(page_obj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listByKeyword(request,keyword,page_num):
    movies = Movie.objects.filter(keywords=keyword)
    paginator = Paginator(movies,12)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = MovieSerializer(page_obj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listByYear(request,year,page_num):
    movies = Movie.objects.filter(releasedate__contains=year)
    paginator = Paginator(movies,12)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = MovieSerializer(page_obj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listByDirctor(request,director,page_num):
    movies = Movie.objects.filter(director=director)
    paginator = Paginator(movies,12)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = MovieSerializer(page_obj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listBynation(request,nation,page_num):
    if nation=="해외":
        movies = Movie.objects.exclude(nation__contains="한국")
    else:
        movies = Movie.objects.filter(nation__contains=nation)

    paginator = Paginator(movies,12)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = MovieSerializer(page_obj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movieSearch(request,word):
    movies = Movie.objects.filter(title__contains=word)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todaymovies(request):
    movies=Movie.objects.all()
    best_movies = Movie.objects.order_by('-ravg')[:5]

    num_list=[]
    random_movies=[]
    while len(num_list)<6:
        num = random.randint(0, 19233)
        if num not in num_list:
            num_list.append(num)
            random_movies.append(movies[num])

    random_serializers = MovieSerializer(random_movies,many=True)
    best_serializers = MovieSerializer(random_movies,many=True)
    return Response({
        'random':random_serializers.data,
        'best':best_serializers.data,
    })

@api_view(['GET'])
def tenmillion(request):
    movie = Movie.objects.filter(Q(movie_id='93756')|Q(movie_id='167651')|Q(movie_id='85579')|Q(movie_id='102875')|Q(movie_id='136900'))
    serializer = MovieSerializer(movie,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movieDetail(request, movie_pk):
    movie = Movie.objects.filter(movie_id=movie_pk)
    serializer = MovieSerializer(movie,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def rate_movie(request,movie_pk):
    movie=get_object_or_404(Movie,movie_id=movie_pk)
    user=request.user
    if Rating.objects.filter(movie_id=movie.movie_id,user_id=user.id).exists():
        rating = Rating.objects.get(movie_id=movie.movie_id,user_id=user.id)
        rating.star=request.data['star']
        rating.save()
    else:
        Rating.objects.create(movie=movie,user=user,star=request.data['star'])

    if request.data['star'] != -1:
        movies=Rating.objects.filter(movie_id=movie_pk).exclude(star=-1)
        movie.rcnt += 1
        movie.rsum += request.data['star']
        movie.ravg = movie.rsum / movie.rcnt
        movie.save()
    return Response()


@api_view(['POST'])
def cancel_rating(request,movie_pk):
    rating = Rating.objects.get(movie_id=movie_pk,user_id=request.user.id)
    rating.delete()
    if request.data['flag']!=1:
        movie=get_object_or_404(Movie,movie_id=movie_pk)
        movie.rcnt -= 1
        movie.rsum -= rating.star
        movie.ravg = movie.rsum/movie.rcnt
        movie.save()
    return Response()

@api_view(['GET'])
def get_rating(request,movie_pk):
    try:
        rating = Rating.objects.get(movie_id=movie_pk,user_id=request.user.id)
        serializer=RatingSerializer(rating)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response()

@api_view(['GET'])
def most_viewed_director(request):
    user = request.user
    rating_movies = Rating.objects.filter(user_id=user).exclude(star=-1).values('movie_id')
    watched_movies = Movie.objects.filter(movie_id__in=rating_movies)
    most_viewed_directors = watched_movies.values('director').annotate(mc=Count('director'))
    most_viewed_director_tmp = most_viewed_directors.aggregate(director = Max('mc'))
    most_viewed_director = most_viewed_directors.filter(mc=most_viewed_director_tmp['director'])[0]['director']

    movies = Movie.objects.filter(director=most_viewed_director).exclude(movie_id__in=rating_movies)
    serializer = MovieSerializer(movies[:5],many=True)
    return Response(serializer.data)

@api_view(['GET'])
def most_viewed_genre(request):
    user = request.user
    rating_movies = Rating.objects.filter(user_id=user).exclude(star=-1).values('movie_id')
    watched_movies = Movie.objects.filter(movie_id__in=rating_movies)
    most_viewed_genres=watched_movies.values('genres').annotate(gc=Count('genres'))
    most_viewed_genre_tmp = most_viewed_genres.aggregate(genre = Max('gc'))
    most_viewed_genre = most_viewed_genres.filter(gc=most_viewed_genre_tmp['genre'])[0]['genres']

    genre = Genre.objects.get(id=most_viewed_genre)
    movies = genre.movie_set.all().exclude(movie_id__in=rating_movies)
    serializer = MovieSerializer(movies[:5],many=True)
    return Response({
        'data':serializer.data,
        'genre_name':most_viewed_genre
        })

@api_view(['GET'])
def most_viewed_keyword(request):
    user = request.user
    rating_movies = Rating.objects.filter(user_id=user).exclude(star=-1).values('movie_id')
    watched_movies = Movie.objects.filter(movie_id__in=rating_movies)
    most_viewed_keywords=watched_movies.values('keywords').annotate(kc=Count('keywords')).order_by('-kc')[0:2]
    movies = Movie.objects.filter(Q(keywords=most_viewed_keywords[0]['keywords'])|Q(keywords=most_viewed_keywords[1]['keywords'])).exclude(movie_id__in=rating_movies)
    serializer = MovieSerializer(movies[:5],many=True)
    return Response({
        'data':serializer.data,
        'keywords':[most_viewed_keywords[0]['keywords'],most_viewed_keywords[1]['keywords']]
        })

@api_view(['GET'])
def most_viewed_actor(request):
    user = request.user
    rating_movies = Rating.objects.filter(user_id=user).exclude(star=-1).values('movie_id')
    watched_movies = Movie.objects.filter(movie_id__in=rating_movies)
    most_viewed_actors=watched_movies.values('actors').annotate(kc=Count('actors')).order_by('-kc')[0:3]
    movies = Movie.objects.filter(Q(actors=most_viewed_actors[0]['actors'])|Q(actors=most_viewed_actors[1]['actors'])|Q(actors=most_viewed_actors[2]['actors'])).exclude(movie_id__in=rating_movies)
    serializer = MovieSerializer(movies[:5],many=True)
    return Response({
        'data':serializer.data,
        'actors':[most_viewed_actors[0]['actors'],most_viewed_actors[1]['actors'],most_viewed_actors[2]['actors']]
        })

@api_view(['GET'])
def recommend_rating_movie(request):
    db = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='ssafy',
        db='ssafyweb',
        charset = 'utf8'
    )

    SQL = 'select * from movies_rating'
    rating_lst_edit = pd.read_sql(SQL,db)
    rating_lst = rating_lst_edit[rating_lst_edit['star'] > 0]
    SQL2 = 'select * from movies_movie'
    movie_lst = pd.read_sql(SQL2,db)
    
    movie_lst=movie_lst.loc[:,'movie_id':'title']

    user_rating_lst = pd.merge(rating_lst,movie_lst,on='movie_id')
    user_movie_rating = user_rating_lst.pivot_table('star',index="movie_id",columns='user_id')
    user_movie_rating.fillna(0,inplace=True)

    item_based_collabor = cosine_similarity(user_movie_rating)
    item_based_collabor = pd.DataFrame(data=item_based_collabor,index=user_movie_rating.index,columns=user_movie_rating.index)
    rating = Rating.objects.filter(user_id=request.user).order_by('star').values()
    title = rating[0]['movie_id']

    rate_lst = item_based_collabor[item_based_collabor.loc[title]>=0.6].index[:]
    movies = Movie.objects.filter(movie_id__in=rate_lst)

    rating_movies = Rating.objects.filter(user_id=request.user).exclude(star=-1).values('movie_id')
    
    serializers = MovieSerializer(movies.exclude(movie_id__in=rating_movies),many=True)

    return Response(serializers.data)


@api_view(['GET'])
def recommend_rating_user(request):
    db = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='ssafy',
        db='ssafyweb',
        charset = 'utf8'
    )

    SQL = 'select * from movies_rating'
    rating_lst_edit = pd.read_sql(SQL,db)
    rating_lst = rating_lst_edit[rating_lst_edit['star'] > 0]
    SQL2 = 'select * from accounts_user'
    user_lst = pd.read_sql(SQL2,db)
    user_lst=user_lst.drop(['password','is_superuser','is_staff','is_active','date_joined','profile_image'],axis=1)
    user_rating_lst = pd.merge(rating_lst,user_lst,left_on='user_id',right_on='id')
    user_movie_rating = user_rating_lst.pivot_table('star',index="user_id",columns='movie_id')
    user_movie_rating.fillna(0,inplace=True)


    item_based_collabor = cosine_similarity(user_movie_rating)
    item_based_collabor = pd.DataFrame(data=item_based_collabor,index=user_movie_rating.index,columns=user_movie_rating.index)
    user = request.user.id
    if item_based_collabor.drop(user,axis=1).loc[user].max()>=0.6:
        similar_user=item_based_collabor.drop(user,axis=1).loc[user].idxmax()
    else:
        return Response()
    
    sim_rating = Rating.objects.filter(user_id=similar_user).exclude(star=-1).values('movie_id')
    movies = Movie.objects.filter(movie_id__in=sim_rating)
    rating_movies = Rating.objects.filter(user_id=request.user).exclude(star=-1).values('movie_id')

    serializers = MovieSerializer(movies.exclude(movie_id__in=rating_movies),many=True)

    return Response(serializers.data)