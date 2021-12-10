from django.contrib import admin

from .models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'deleted_at']
    list_filter = ['id']
    search_fields = ['id']
    ordering = ['-created']


admin.site.register(Topic, TopicAdmin)
