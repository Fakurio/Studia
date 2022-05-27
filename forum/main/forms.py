from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    field_order = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]