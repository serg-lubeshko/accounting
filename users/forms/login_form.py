from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import MyUser


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control py-4",
            # "id": "inputEmailAddress",
            "placeholder": "Введите имя пользователя",

        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control py-4",
            # "id": "inputPassword",
            "placeholder": "Введите пароль",
        }
    ))

    class Meta:
        model = MyUser
        fields = ("username", "password")


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control py-4",
            # "id": "inputEmailAddress",
            "placeholder": "Введите имя пользователя",

        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control py-4",
            # "id": "inputPassword",
            "placeholder": "Введите пароль",
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control py-4",
            # "id": "inputPassword",
            "placeholder": "Подтвердите пароль",
        }
    ))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control py-4",
            "placeholder": "Введите имя",

        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control py-4",
            "placeholder": "Введите фамилию",

        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            "class": "form-control py-4",
            "placeholder": "Введите адрес эл. почты",

        }
    ))

    class Meta:
        model = MyUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password2",
            "password1"
        )
