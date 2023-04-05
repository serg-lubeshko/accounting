from datetime import datetime

from django.db.models import Sum, FloatField

from accounting.models import Balance, BasketExpenses
from utils_project.services import remaining_days_in_month


def nav_context(request):
    # TODO переделать. Необходимо счет подвязать к юзеру, найти решение по карте, т.к здесь хардкор
    card_sum = Balance.objects.first()
    total_expenses_month = \
        BasketExpenses.objects.filter(date__month=datetime.now().month).aggregate(sum_expenses=Sum('total'))[
            'sum_expenses']
    cash_back = BasketExpenses.objects.select_related('category', 'good').filter(
        date__month=datetime.now().month,
        card=1,
        store__store_code__in=[5199, 5297, 5298, 5299, 5311, 5331, 5411, 5412, 5415, 5422, 5441, 5451, 5462, 5131, 5137,
                               5139, 5611, 5621, 5631, 5641, 5651, 5661, 5681, 5691, 5697, 5698, 5699, 5931, 7251, 7278,
                               7296]
    ).aggregate(sum_cash=Sum('total'),
                cash_back=Sum('total', output_field=FloatField()) * 0.025
                )
    data = {
        'card_sum': card_sum,
        'total_expenses_month': total_expenses_month,
        'remaining_days': remaining_days_in_month(),
        'sum_cash_back': cash_back['sum_cash'],
        'cash_back': cash_back['cash_back']

    }
    return data
