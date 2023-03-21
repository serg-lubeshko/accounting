from datetime import datetime

from django.db.models import Sum, Q
from django.views import generic

from accounting import models


class ExpensesList(generic.ListView):
    """
    Выводим список покупок
    """

    model = models.BasketExpenses
    paginate_by = 10
    context_object_name = 'expenses_lists'
    template_name = 'accouting/baskets_expenses.html'
    ordering = "-date"
    # queryset = models.BasketExpenses.objects.filter(date=datetime.utcnow())
    queryset = models.BasketExpenses.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.GET.get('date')
        if date or self.kwargs.get('date'):
            queryset = queryset.filter(date=date)
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top_products = models.BasketExpenses.objects.values('category', 'category__category_name').annotate(
            sum_cat=Sum('total', filter=Q(date__month=datetime.now().month))).order_by('-sum_cat')
        context['top_products'] = top_products.exclude(sum_cat__isnull=True).exclude(sum_cat=0)
        context['total_amount'] = sum(expenses.total for expenses in context['expenses_lists'])
        context['cur_date'] = self.request.GET.get('date')
        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(user=self.request.user)
