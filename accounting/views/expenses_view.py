from datetime import datetime

from django.db.models import Sum, Q
from django.views import generic

from accounting import models


class ExpensesList(generic.ListView):
    """
    Выводим список покупок
    """

    model = models.BasketExpenses
    paginate_by = 100  # if pagination is desired
    context_object_name = 'expenses_lists'
    template_name = 'accouting/baskets_expenses.html'
    ordering = "-date"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_products'] = models.BasketExpenses.objects.values('category', 'category__category_name').annotate(
            sum_cat=Sum('total', filter=Q(date__month=datetime.now().month))).order_by('category')[:5]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
