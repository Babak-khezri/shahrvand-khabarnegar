from django.contrib import admin
from .models import Reportage
# Register your models here.


class ReportageAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date', 'pk', 'likes_count')


admin.site.register(Reportage, ReportageAdmin)
