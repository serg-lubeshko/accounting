from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.forms.django_views_form import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username, password)
            if user:
                auth.login(request, user)  # +разрешения
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context=context)


def registration(request):
    return render(request, 'users/registration.html')