from django.urls import path, register_converter

from accounting.views.create_expenses import CreateExpensesView
from accounting.views.create_income_source_view import CreateSourceIncomeView, AddSourceIncomeView
from accounting.views.create_store import CreateStoreView
from accounting.views.delete_expenses import DeleteItemView
from accounting.views.expenses_view import ExpensesList, ExpensesNewList
from utils_project.converter import DateConverter

app_name = 'accounting'

register_converter(DateConverter, 'date')

urlpatterns = [
    # path("", basket_expenses, name="basket_expenses"),
    path("", ExpensesList.as_view(), name="basket_expenses"),
    path("list/", ExpensesNewList.as_view(), name="basket_expenses_list"),
    path("list/<date:front_date>/", ExpensesNewList.as_view(), name="basket_expenses_list"),
    # path("/<str:date>", ExpensesList.as_view(), name="basket_expenses"),
    # path("add-expenses/", AddExpensesView.as_view(), name="add-expenses"),
    path("create-expenses/", CreateExpensesView.as_view(), name="create-expenses"),
    path("create-store/", CreateStoreView.as_view(), name="create-store"),
    path("create-source-income/", CreateSourceIncomeView.as_view(), name="create-income"),
    path("add-source-income/", AddSourceIncomeView.as_view(), name="add-income"),
    path("delete-expenses/<int:pk>", DeleteItemView.as_view(), name="delete-expenses"),

]
