from django.contrib import admin

from .models import AcademicYear


class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ['id', 'created']
    list_filter = ['id']
    search_fields = ['id']
    ordering = ['-created']

admin.site.register(AcademicYear, AcademicYearAdmin)