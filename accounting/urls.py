from django.urls import path


from accounting.views.expenses_view import ExpensesList

app_name = 'users'

urlpatterns = [
    # path("", basket_expenses, name="basket_expenses"),
    path("", ExpensesList.as_view(), name="basket_expenses"),

]
