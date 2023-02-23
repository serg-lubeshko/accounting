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
    ordering = "id"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
