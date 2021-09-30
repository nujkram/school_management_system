from django import forms
from departments.models.department.models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'code')
