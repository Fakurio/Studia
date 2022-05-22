from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    field_order = ["username","email","password1","password2"]
    