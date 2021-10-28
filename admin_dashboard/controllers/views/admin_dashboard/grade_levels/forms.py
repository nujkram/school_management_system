from django import forms
from grade_levels.models.grade_level.models import GradeLevel


class GradeLevelForm(forms.ModelForm):
    class Meta:
        model = GradeLevel
        fields = ('name', 'code')
