from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Userr

from django import forms


class CreateUserForm(UserCreationForm):
   
    class Meta:
	    model = Userr
	    fields = ['empid','name','email','password1','password2']