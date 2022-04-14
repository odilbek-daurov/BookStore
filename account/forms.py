from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import MyUser


class UserCreate(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password1', 'password2']


class Profile(ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'email']