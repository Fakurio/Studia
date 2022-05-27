from django.shortcuts import render, redirect
from .forms import PostForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.

@login_required(login_url="/login")
def home(response):
    posts = Post.objects.all()

    if response.method == "POST":
        post_id = response.POST.get("post-id")
        post = Post.objects.get(id=post_id)
        if post and post.author == response.user:
            post.delete()
            
    return render(response, "main/home.html", {"posts": posts})

@login_required(login_url="/login")
def create_post(response):
    if response.method == "POST":
        form = PostForm(response.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = response.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()

    return render(response, "main/create_post.html", {"form": form})

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