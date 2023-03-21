from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounting.forms import SourceIncomeForm


class CreateSourceIncomeView(CreateView):
    template_name = "accouting/form_source_income.html"
    form_class = SourceIncomeForm

    success_url = reverse_lazy('accounting:basket_expenses')

    # def get_success_url(self):
    #     return self.request.META.get('HTTP_REFERER')
