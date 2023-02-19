from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.forms.login_form import UserLoginForm, UserRegistrationForm
from users.forms.profile_form import UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)  # +разрешения
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались!")
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context=context)


def profile(request):
    if request.method == 'POST':
        print(request.POST, 'efwewf')
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    try:
        form = UserProfileForm(instance=request.user)
    except AttributeError:
        return HttpResponseRedirect(reverse('users:login'))
    context = {
        'title': 'CostA - Профиль',
        'form': form
    }

    return render(request=request, template_name="users/profile.html", context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("users:login"))
