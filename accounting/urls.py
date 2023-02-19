from django.urls import path

from accounting.views import basket_expenses

app_name = 'users'

urlpatterns = [
    path("", basket_expenses, name="basket_expenses"),

]
