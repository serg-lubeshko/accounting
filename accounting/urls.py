from django.urls import path

from accounting.views.add_expenses import AddExpensesView
from accounting.views.create_expenses import CreateExpensesView
from accounting.views.create_income_source_view import CreateSourceIncomeView
from accounting.views.create_store import CreateStoreView
from accounting.views.delete_expenses import DeleteItemView
from accounting.views.expenses_view import ExpensesList

app_name = 'accounting'

urlpatterns = [
    # path("", basket_expenses, name="basket_expenses"),
    path("", ExpensesList.as_view(), name="basket_expenses"),
    # path("/<str:date>", ExpensesList.as_view(), name="basket_expenses"),
    # path("add-expenses/", AddExpensesView.as_view(), name="add-expenses"),
    path("create-expenses/", CreateExpensesView.as_view(), name="create-expenses"),
    path("create-store/", CreateStoreView.as_view(), name="create-store"),
    path("create-source-income/", CreateSourceIncomeView.as_view(), name="create-income"),
    path("delete-expenses/<int:pk>", DeleteItemView.as_view(), name="delete-expenses"),

]
