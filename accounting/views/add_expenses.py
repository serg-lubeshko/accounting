from django.views.generic import TemplateView


class AddExpensesView(TemplateView):
    template_name = 'accounting/create_acounting.html'
