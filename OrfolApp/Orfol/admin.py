from django.contrib import admin
from .models import Category
from .models import Subcategory
from .models import Report
from .models import Profile


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Report)
admin.site.register(Profile)