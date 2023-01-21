
from django.urls import path

from users.views.django_views_login import login, registration

app_name = 'users'

urlpatterns = [
    path("login/", login, name="login"),
    path("registration/", registration, name="registration"),
]
