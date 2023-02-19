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
