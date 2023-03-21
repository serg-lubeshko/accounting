from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounting.forms import CreateExpensesForm
from accounting.models import BasketExpenses
from django.contrib import messages

class CreateExpensesView(CreateView):
    template_name = "accouting/create_acounting.html"
    form_class = CreateExpensesForm
    success_url = reverse_lazy('accounting:basket_expenses')
    # model = BasketExpenses

    # def get_success_url(self):
    #     date = self.request.POST.get('date', None)
    #     if date:
    #         success_url = reverse_lazy('accounting:basket_expenses', kwargs={'date': date})
    #     else:
    #         success_url = reverse_lazy('accounting:basket_expenses')
    #     return f"{self.success_url}?date={date}"


    def form_valid(self, form):
        print('HERER')
        # Получить объект BasketExpenses из формы, но не сохранять его
        expenses = form.save(commit=False)
        # Установить текущего пользователя как user в BasketExpenses
        expenses.user = self.request.user
        # Вызвать метод save() для сохранения BasketExpenses
        # expenses.save()

        if form.errors:
            messages.error(self.request, 'Форма заполнена неправильно.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(self.request, f'{field}: {error}')

        date = form.cleaned_data.get('date')
        if date:
            # Append the date parameter to the success URL as a query parameter
            self.success_url = f"{self.success_url}?date={date}"
        return super().form_valid(form)

