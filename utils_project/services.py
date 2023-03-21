from datetime import date, timedelta

def remaining_days_in_month():
    """
    Остаток дней в текущем месяце.
    Начинаем с текущей даты (today) и заменяем ее день на первое число месяца, используя метод replace(day=1).
    Затем мы добавляем к этой дате 32 дня, используя timedelta(days=32).
    Добавление 32 дней обеспечивает достаточное количество дней для того, чтобы обеспечить переход на следующий месяц

    """

    today = date.today()
    days_in_month = (today.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    days_left = days_in_month.day - today.day
    return days_left
