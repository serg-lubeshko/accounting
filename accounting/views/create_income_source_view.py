from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounting.forms import SourceIncomeForm, AddSourceIncomeForm


class CreateSourceIncomeView(CreateView):
    template_name = "accounting/form_source_income.html"
    form_class = SourceIncomeForm

    success_url = reverse_lazy('accounting:add-income')

    # def get_success_url(self):
    #     return self.request.META.get('HTTP_REFERER')


class AddSourceIncomeView(CreateView):
    """
    Создаем корзину доходов
    """
    template_name = "accounting/form_bascket_income.html"
    form_class = AddSourceIncomeForm

    success_url = reverse_lazy('accounting:add-income')

    def form_valid(self, form):
        income = form.save(commit=False)
        income.user = self.request.user

        if form.errors:
            messages.error(self.request, 'Форма заполнена неправильно.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(self.request, f'{field}: {error}')

        return super().form_valid(form)
