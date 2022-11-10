from django.db import models


class Store(models.Model):
    """ Магазин """

    store_id = models.BigAutoField(primary_key=True, verbose_name="id")
    store_name = models.CharField(max_length=255, verbose_name="Название магазина")

    def __str__(self):
        return self.store_name

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

    def __str__(self):
        return self.good_name


class Category(models.Model):
    """ Категория расхода/дохода """

    category_id = models.BigAutoField(primary_key=True, verbose_name="id")
    category_name = models.CharField(max_length=255, verbose_name="Название категории")
    #выбор чоиса на доход/расход
    #picture
    #user
    #дата создания

    def __str__(self):
        return self.category_name

