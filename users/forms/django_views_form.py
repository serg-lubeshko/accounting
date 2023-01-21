from django.contrib.auth.forms import AuthenticationForm

from users.models import MyUser


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ("username", "password")