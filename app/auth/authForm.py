from django import forms
from .. import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# SetPasswordForm
# from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
# from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
# from django.contrib.auth import password_validation


class Register(UserCreationForm):
    """
    Display the registration form based on given fields
    """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'id': 'InputUname',
                   'placeholder': 'User Name'}),
        max_length=32,
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'id': 'InputEmail',
                   'placeholder': 'Email Address'}),
        max_length=254,
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'id': 'InputPassword',
                   'placeholder': 'Password'})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'id': 'InputPassword',
                   'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = models.User
        fields = ['username', 'email', 'password1', 'password2']


class Login(AuthenticationForm):
    """
    Display the login form based on the given fields
    """
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'id': 'InputEmail',
                   'placeholder': 'User Name'}),
        max_length=254)

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'id': 'InputPassword',
                   'placeholder': 'Password'})
    )
