from datetime import datetime

from django.db.models import Sum

from accounting.models import Balance, BasketExpenses
from calendar import monthrange

from utils_project.services import remaining_days_in_month


def nav_context(request):
    #TODO переделать. Необходимо счет подвязать к юзеру
    card_sum = Balance.objects.first()
    total_expenses_month = BasketExpenses.objects.filter(date__month=datetime.utcnow().month).aggregate(sum_expenses=Sum('total'))['sum_expenses']
    data = {
        'card_sum': card_sum,
        'total_expenses_month': total_expenses_month,
        'remaining_days': remaining_days_in_month()


    }
    return data