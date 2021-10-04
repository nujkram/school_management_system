from django import forms
from subjects.models.subject.models import Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name', 'code', 'department', 'year_level')
