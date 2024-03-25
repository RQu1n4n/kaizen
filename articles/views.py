from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.

def all_articles(request):
    article_list = Article.objects.all().order_by('title')
    return render(request, 'article_list.html', {'article_list': article_list})


def home(request):
    return render(request, 'home.html', {})

def user_registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, 'Account Created Successfully')
            
    context = {'form':form}
    return render(request, 'register.html', context)

def user_login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
           user = form.get_user()
           login(request, user)
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html')
