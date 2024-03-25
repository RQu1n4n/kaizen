from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles', views.all_articles, name="article_list"),
    path('login', views.user_login, name="login"),
    path('signup', views.user_registration, name="register"),
]
