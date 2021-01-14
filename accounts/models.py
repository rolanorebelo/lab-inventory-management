from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Userr(AbstractBaseUser):
   
    password = None
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    username = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=200, null=True)
    password2 = models.CharField(max_length=200, null=True)