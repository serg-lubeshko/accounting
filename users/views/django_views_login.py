from django.shortcuts import render

from users.forms.django_views_form import UserLoginForm


def login(request):
    context ={
        'form': UserLoginForm()
    }
    return render(request, 'users/login.html', context=context)


def registration(request):
    return render(request, 'users/registration.html')