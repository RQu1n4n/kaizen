from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('articles', views.all_articles, name="article_list"),
    path('login', views.login, name="login"),
    path('sign-up', views.sign_up, name="sign-up"),
    path('about', views.about, name="about"),
    path('register/', views.register, name="reg"),
    path('login/', views.user_login, name="log")
]
