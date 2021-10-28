from django import forms
from academic_years.models.academic_year_subject.models import AcademicYearSubject


class AcademicYearSubjectForm(forms.ModelForm):
    class Meta:
        model = AcademicYearSubject
        fields = ('academic_year', 'subject', 'grade_level', 'section', 'faculty')
