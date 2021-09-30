from django.contrib import admin

from .models import Section


class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'created']
    list_filter = ['id']
    search_fields = ['id']
    ordering = ['-created']

admin.site.register(Section, SectionAdmin)