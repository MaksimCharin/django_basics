from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}))

    def __init__(self, *args, **kwargs):
        super(CustomUserAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        username = self.cleaned_data.get('username')
        if username and '@' not in username:
            raise forms.ValidationError("Введите корректный адрес электронной почты.")
        return super().clean()