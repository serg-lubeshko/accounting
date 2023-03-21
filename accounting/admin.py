from django.contrib import admin

from accounting.models import Store, Code, Measure, Good, Category, BasketExpenses, Card, Balance, SourceIncome, \
    BasketIncome

# admin.site.register(Store)
admin.site.register(Code)
admin.site.register(Measure)
admin.site.register(Good)
admin.site.register(Category)
admin.site.register(BasketExpenses)
admin.site.register(Card)
admin.site.register(Balance)
admin.site.register(SourceIncome)
admin.site.register(BasketIncome)



class StoreAdmin(admin.ModelAdmin):
    model = Store
    list_display = ("store_name", "store_code")
    ordering = ('store_name',)


admin.site.register(Store, StoreAdmin)