from django.contrib import admin

from accounting.models import Store, Code, Measure, Good, Category

admin.site.register(Store)
admin.site.register(Code)
admin.site.register(Measure)
admin.site.register(Good)
admin.site.register(Category)
