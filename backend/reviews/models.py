from django.db import models
from django.conf import settings
from movies.models import Movie

# Create your models here.

class Review(models.Model):
    writer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)
    summary=models.CharField(max_length=500)
    content=models.TextField()
    spo=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    

class Comment(models.Model):
    writer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    review=models.ForeignKey(Review,on_delete=models.CASCADE)
    content=models.CharField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)