from django.urls import path
from .views import account_login, signup, logout_view

urlpatterns = [
    path('login/',account_login, name='account_login'),
    path('create/',signup, name='signup'),
    path('logout/',logout_view, name='logout'),
]