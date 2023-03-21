from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounting.forms import CreateStoreForm


class CreateStoreView(CreateView):
    template_name = "accouting/form_store.html"
    form_class = CreateStoreForm

    success_url = reverse_lazy('accounting:basket_expenses')

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
