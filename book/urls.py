from django.contrib import admin
from django.urls import path
from .views import home, detail, like, author_book, language_book, category_book

urlpatterns = [
    path('', home, name='home'),
    path('detail/<slug:slug>', detail, name='detail'),
    path('liked/<slug:slug>', like, name='liked'),
    path('author/<str:slug>', author_book, name='author_book'),
    path('language/<slug:slug>', language_book, name='language_book'),
    path('cayegory/<slug:slug>', category_book, name='category_book'),
]