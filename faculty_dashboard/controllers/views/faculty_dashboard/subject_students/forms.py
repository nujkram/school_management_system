from django import forms
from subjects.models.subject_student.models import SubjectStudent


class SubjectStudentForm(forms.ModelForm):
    class Meta:
        model = SubjectStudent
        fields = ('subject', 'student')
