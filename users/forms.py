from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    usable_password = None
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


# class UserLoginForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('email', 'password1', 'password2')
