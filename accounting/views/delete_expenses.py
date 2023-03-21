from django.views import generic

from accounting import models


class DeleteItemView(generic.DeleteView):
    model = models.BasketExpenses
    success_url = "/"
    template_name = 'accouting/baskets_expenses.html'
