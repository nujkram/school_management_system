from django import forms
from academic_years.models.academic_year_subject.models import AcademicYearSubject


class AcademicYearSubjectForm(forms.ModelForm):
    class Meta:
        model = AcademicYearSubject
        fields = '__all__'
