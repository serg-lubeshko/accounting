from django.db import transaction
from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from accounting.models import BasketExpenses, Balance, BasketIncome


@receiver([post_save], sender=BasketExpenses)
@transaction.atomic
def post_save_basket(**kwargs):
    print(12121221)
    sum_total = kwargs['instance'].total
    obj_card = Balance.objects.get(card=kwargs['instance'].card)
    obj_card.cur_summ_balance = F('cur_summ_balance') - sum_total
    obj_card.save()

#TODO убрать дублирование
@receiver([post_delete], sender=BasketExpenses)
def delete_good_basket(**kwargs):
    sum_total = kwargs['instance'].total
    obj_card = Balance.objects.get(card=kwargs['instance'].card)
    obj_card.cur_summ_balance = F('cur_summ_balance') + sum_total
    obj_card.save()


@receiver([post_save], sender=BasketIncome)
def save_income_basket(**kwargs):
    print(kwargs['instance'], 'ttt')
    sum_total = kwargs['instance'].sum_income
    obj_card = Balance.objects.get(card=kwargs['instance'].card)
    obj_card.cur_summ_balance = F('cur_summ_balance') + sum_total
    obj_card.save()

