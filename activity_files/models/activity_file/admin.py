from django.contrib import admin

from .models import ActivityFile


class ActivityFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'created']
    list_filter = ['id']
    search_fields = ['id']
    ordering = ['-created']

admin.site.register(ActivityFile, ActivityFileAdmin)