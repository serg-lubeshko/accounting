from django import forms

from accounting import models


class BasketExpensesForms(forms.ModelForm):
    class Meta:
        model = models.BasketExpenses
        fields = (
            'category',
            'good',
            'count',
            'cost',
            'date'
        )

        widgets = {
            "category": forms.TextInput(attrs={"class": "form-control"}),
            "good": forms.TextInput(attrs={"class": "form-control"}),
            "count": forms.TextInput(attrs={'class': 'form-control'}),
            "date": forms.DateInput(attrs={'class': 'form-control'}),

        }