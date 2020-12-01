from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    id = models.CharField(max_length=10,primary_key=True)

class Actor(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class Keyword(models.Model):
    keyword = models.CharField(max_length=100, primary_key=True) 

class Movie(models.Model):
    movie_id = models.CharField(max_length=20,primary_key=True)
    title = models.CharField(max_length=200, null=True)
    titleorigin = models.CharField(max_length=200,null=True)
    genres = models.ManyToManyField(Genre,blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    nation = models.CharField(max_length=100, null=True)
    # runtime = models.CharField(max_length=10, null=True)
    releasedate = models.CharField(max_length=200,null=True)
    director = models.CharField(max_length=100, null=True)
    # directorid = models.IntegerField(null=True)
    # video = models.TextField(null=True)
    poster = models.TextField(null=True)
    plot = models.TextField(null=True)
    rate = models.CharField(max_length=100,null=True)
    ratecnt = models.TextField(null=True)
    rsum=models.FloatField(null=True)
    ravg=models.FloatField(null=True)
    rcnt=models.IntegerField(null=True)

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    star = models.FloatField()