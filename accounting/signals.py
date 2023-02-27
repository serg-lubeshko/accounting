from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounting.models import BasketExpenses, Balance


@receiver([post_save], sender=BasketExpenses)
def post_save_basket(**kwargs):
    sum_total = kwargs['instance'].total
    obj_card = Balance.objects.get(card=kwargs['instance'].card)
    obj_card.cur_summ_balance = F('cur_summ_balance') - sum_total
    obj_card.save()
    # pk_doc = kwargs['instance'].doc_id_id
    # quer = DocLock.objects.filter(doc_id=pk_doc)
    # if quer.count() > 0:
    #     users = list(quer.values_list('update_user', flat=True))
    #     raise exceptions.ParseError(f"{REPLY_TEXTS[11]} {users}")
