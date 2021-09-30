from django import forms
from year_levels.models.year_level.models import YearLevel


class YearLevelForm(forms.ModelForm):
    class Meta:
        model = YearLevel
        fields = ('name', 'code',)
