from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def all_articles(request):
    article_list = Article.objects.all().order_by('title')
    return render(request, 'article_list.html', {'article_list': article_list})

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def sign_up(request):
    return render(request, 'register.html', {})

def login(request):
    return render(request, 'login.html', {})

def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        user = KaizenUser.objects.create_user(first_name=firstname, last_name=lastname,
                                              email=email, password=password)
        user.save()
        print(user.email, user.password)
        return redirect('login')
    else:
        return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
