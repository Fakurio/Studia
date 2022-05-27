from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home(response):
    return render(response, "main/home.html")

def sign_up(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            login(response, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(response, "registration/sign_up.html", {"form": form})