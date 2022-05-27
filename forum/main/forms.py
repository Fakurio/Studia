from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    field_order = ["username", "email", "password1", "password2"]