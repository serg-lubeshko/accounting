
from django.urls import path

from users.views.login_views_django import login, registration

app_name = 'users'

urlpatterns = [
    path("login/", login, name="login"),
    path("registration/", registration, name="registration"),
]
