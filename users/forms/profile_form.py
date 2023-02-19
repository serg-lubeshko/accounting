from django import forms
from django.contrib.auth.forms import UserChangeForm

from users import models


class UserProfileForm(UserChangeForm):
    # first_name = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control py-4',
    #     }
    # ))
    # last_name = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control py-4',
    #     }
    # ))
    # email = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control py-4',
    #         'readonly': True
    #     }
    # ))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": 'custom-file-input', 'required': True}))

    # username = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control py-4',
    #         'readonly': True
    #     }
    # ))

    class Meta:
        model = models.MyUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "image"

        )
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control py-4"}),
            "last_name": forms.TextInput(attrs={"class": "form-control py-4"}),
            "email": forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}),
            "username": forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}),

        }
