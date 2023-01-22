from django import forms
from django.contrib.auth.forms import AuthenticationForm

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
