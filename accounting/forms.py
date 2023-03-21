from datetime import datetime

from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms

from accounting import models


# class DateInput(DatePickerInput):
#
#     format = '%d.%m.%Y'

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


class CreateExpensesForm(forms.ModelForm):
    widgets_attrs = {
        'class': 'form-control'
    }

    date = forms.DateField(widget=DatePickerInput(options={
        'format': 'DD-MM-YYYY',
    }))

    count = forms.IntegerField(required=False)

    class Meta:
        model = models.BasketExpenses
        fields = (
            'category',
            'good',
            'count',
            'cost',
            'date',
            'card',
            'store'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['date'].initial = datetime.now().date()
        self.fields['store'].required = False
        self.fields['good'].required = False

        # # Добавляем класс CSS в атрибут class виджета cost
        # self.fields['store'].widget.attrs['class'] = 'input-with-store-icon'

        for field_name, field in self.fields.items():
            widget = field.widget
            widget.attrs.update(self.widgets_attrs)


class BaseForm(forms.ModelForm):
    widgets_attrs = {
        'class': 'form-control'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            widget = field.widget
            widget.attrs.update(self.widgets_attrs)


class CreateStoreForm(BaseForm):
    class Meta:
        model = models.Store
        fields = (
            'store_name',
            'store_code',
        )


class SourceIncomeForm(BaseForm):
    class Meta:
        model = models.SourceIncome
        fields = (
            'source_name',
        )
