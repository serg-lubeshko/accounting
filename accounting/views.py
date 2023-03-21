from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import BasketExpensesForms


# def  basket_expenses(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = BasketExpensesForms(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             print(form.cleaned_data)
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = BasketExpensesForms()
#
#     return render(request, 'accouting/baskets_expenses.html', {'form': form})
