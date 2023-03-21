from django.views.generic import TemplateView


class AddExpensesView(TemplateView):
    template_name = 'accouting/create_acounting.html'
