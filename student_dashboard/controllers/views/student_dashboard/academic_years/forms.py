from django import forms
from academic_years.models.academic_year.models import AcademicYear


class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = '__all__'
