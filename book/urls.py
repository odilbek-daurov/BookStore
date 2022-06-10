from django.contrib import admin
from django.urls import path
from .views import home, detail, like, author_book, language_book, category_book, likes, home_list

urlpatterns = [
    path('home/', home, name='home'),
    path('', home_list, name='home_list'),
    path('detail/<slug:slug>', detail, name='detail'),
    path('liked/<slug:slug>', like, name='liked'),
    path("likes/", likes, name="like"),
    
    path('author/<str:slug>', author_book, name='author_book'),
    path('language/<slug:slug>', language_book, name='language_book'),
    path('cayegory/<slug:slug>', category_book, name='category_book'),


]