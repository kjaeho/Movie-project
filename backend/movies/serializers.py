from rest_framework import serializers
# from accounts.serializers import UserSerializer
from .models import Movie, Genre, Actor, Keyword, Rating

class MovieSerializer(serializers.ModelSerializer):
    # genres = GenreSerializer(many=True,read_only=True)
    # like_users = UserSerializer(read_only=True,required=False)
    # visited_users = UserSerializer(read_only=True,required=False)
    class Meta:
        model = Movie
        # fields = ('title','release_date','overview','vote_count','vote_average','genres','popularity','poster_path',)
        fields='__all__'
        # exclude = ('like_users','visited_users')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'