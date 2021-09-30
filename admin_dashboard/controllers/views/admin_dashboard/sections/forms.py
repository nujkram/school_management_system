from django import forms
from sections.models.section.models import Section


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ('name', 'code', 'is_active')
