from django.shortcuts import render, redirect
from .forms import PostForm, RegisterForm
from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Post
# Create your views here.

@login_required(login_url="/login")
def home(response):
    posts = Post.objects.all()

    if response.method == "POST":
        post_id = response.POST.get("post-id")
        user_id = response.POST.get("user-id")

        if post_id:
            post = Post.objects.get(id=post_id)
            if post and (post.author == response.user or response.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.get(id=user_id)
            if user and response.user.is_staff:
                group = Group.objects.get(name="default")
                group.user_set.remove(user)
                group = Group.objects.get(name="mod")
                group.user_set.remove(user)
                messages.add_message(response, messages.SUCCESS, "User was successfully banned")

    return render(response, "main/home.html", {"posts": posts})


@login_required(login_url="/login")
@permission_required("main.add_post", login_url="/login", raise_exception=True)
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