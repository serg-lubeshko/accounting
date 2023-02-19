
from django.urls import path

from users.views.login_views_django import login, registration, profile, logout

app_name = 'users'

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("registration/", registration, name="registration"),
    path("profile/", profile, name="profile"),
]
