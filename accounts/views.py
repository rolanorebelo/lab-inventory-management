from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.

from .models import *
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, manager_only

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			name = form.cleaned_data.get('name')

			group = Group.objects.get(name='users')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + name)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password =request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

def forgotPassword(request):
    context = {}
    return render(request, 'accounts/password_reset.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@manager_only
def homePage(request):
    context = {}
    return render(request, 'accounts/home.html', context)

def userPage(request):
	context = {}
	return render(request, 'accounts/user.html', context)