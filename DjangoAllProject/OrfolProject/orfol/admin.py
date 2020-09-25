from django.contrib import admin
from .models import ReportImage,Report,SavedReport,Category,SubCategory,Notification

admin.site.register(Report)
admin.site.register(ReportImage)
admin.site.register(SavedReport)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Notification)
