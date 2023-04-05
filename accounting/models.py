import datetime

from django.core.validators import MinValueValidator
from django.db import models

from users.models import MyUser


class Balance(models.Model):
    """ Баланс для карт"""

    cur_summ_balance = models.DecimalField(max_digits=20,
                                           decimal_places=2,
                                           verbose_name="Текущий баланс")
    date_last_trans = models.DateTimeField(auto_now=True, verbose_name="Последняя транзакция")

    def __str__(self):
        return f"{self.cur_summ_balance}"


class Card(models.Model):
    """ Карт-Счет"""

    CURRENCY = (
        ('BYN', 'BYN'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
        ('CNY', 'CNY'),
    )
    card_name = models.CharField(max_length=125, verbose_name="Название карты")
    local_cur = models.BooleanField(default=True)
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY,
        default="BYN",
    )
    beg_balance = models.DecimalField(max_digits=20,
                                      decimal_places=2,
                                      verbose_name="Начальный баланс",
                                      default=0)

    cur_balance = models.OneToOneField(Balance, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.card_name} || {self.cur_balance} {self.currency}"


class Store(models.Model):
    """ Магазин """

    store_id = models.BigAutoField(primary_key=True, verbose_name="id")
    store_name = models.CharField(max_length=255, verbose_name="Название магазина")
    store_code = models.IntegerField(verbose_name="Код МСИ", blank=True, null=True)

    def __str__(self):
        return f"{self.store_name} | {self.store_code}"


class Code(models.Model):
    """ Шифр товара """

    code_id = models.BigAutoField(primary_key=True, verbose_name="id")
    code_name = models.CharField(max_length=255, verbose_name="Код")
    store = models.ForeignKey(Store, on_delete=models.PROTECT, verbose_name="Шифр товара")

    class Meta:
        unique_together = ("store", "code_name")

    def __str__(self):
        return self.code_name


class Measure(models.Model):
    """ Единица измерения """

    measure_id = models.BigAutoField(primary_key=True, verbose_name="id")
    measure_name = models.CharField(max_length=55, verbose_name="Единица измерения")

    def __str__(self):
        return self.measure_name


class Good(models.Model):
    """ Товар """

    good_id = models.BigAutoField(primary_key=True, verbose_name="id")
    good_name = models.CharField(max_length=255, verbose_name="Название товара")
    # code = models.ForeignKey(Code, on_delete=models.PROTECT, verbose_name="Шифр товара")
    measure = models.ForeignKey(Measure, on_delete=models.DO_NOTHING, blank=True, null=True)
    good_parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.good_name


class Category(models.Model):
    """ Категория расхода """

    category_id = models.BigAutoField(primary_key=True, verbose_name="id")
    category_name = models.CharField(max_length=255, verbose_name="Название категории")

    # выбор чоиса на доход/расход
    # picture
    # user
    # дата создания

    def __str__(self):
        return self.category_name


class BasketExpenses(models.Model):
    """
    Корзина расходов
    """
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория", related_name='category')
    good = models.ForeignKey(Good, on_delete=models.PROTECT, verbose_name="Товар", blank=True, null=True,
                             related_name='good_basket')
    count = models.PositiveIntegerField(verbose_name="Количество", default=1)
    cost = models.DecimalField(verbose_name='Стоимость', max_digits=8, decimal_places=2, default=0,
                               validators=[MinValueValidator(0)])
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT, verbose_name="Пользователь")
    date = models.DateField(verbose_name="Дата")
    total = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, default=0, verbose_name="Всего")
    basket = models.PositiveIntegerField(blank=True, null=True)
    card = models.ForeignKey(Card, on_delete=models.PROTECT, verbose_name="Карта")
    store = models.ForeignKey(Store, on_delete=models.PROTECT, verbose_name="Магазины", blank=True, null=True)

    def __str__(self):
        return f"{self.category}| {self.good}| {self.count}"

    def save(self, *args, **kwargs):
        if getattr(self, 'cost', 0):
            self.total = self.count * self.cost
        super().save(*args, **kwargs)


class BasketIncome(models.Model):
    """
    Корзина Доходы
    """
    card = models.ForeignKey(Card, on_delete=models.PROTECT, verbose_name="Карта")
    date = models.DateField(verbose_name="Дата поступления", default=datetime.datetime.utcnow)
    sum_income = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Сумма поступления")
    source_income = models.ForeignKey("SourceIncome", on_delete=models.PROTECT, verbose_name="Источник дохода")
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT, verbose_name="Юзер")

    def __str__(self):
        return f"{self.source_income}| {self.sum_income}"


class SourceIncome(models.Model):
    """
    Источник дохода
    """
    source_name = models.CharField(max_length=255, verbose_name="Название источника")

    def __str__(self):
        return self.source_name
