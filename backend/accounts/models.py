from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     profileimg = models.TextField(blank=True)
class User(AbstractUser):
    first_name=None
    last_name=None
    # username = None
    # is_staff = None
    last_login = None
    profile_image = models.CharField(max_length=400,blank=True)
    # nickname = models.CharField(max_length=100)
    email = models.CharField(max_length=255,unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    