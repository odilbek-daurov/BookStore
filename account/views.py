from django.shortcuts import render, redirect
from .forms import UserCreate, Profile
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserCreate(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('account_login')

    else:
        form = UserCreate()

    return render(request, 'register/create_account.html', {'form': form})


def account_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'register/login_page.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def checkout(request):
    form = Profile(request.user)
    return render(request, 'checkout.html', {'form': form})



