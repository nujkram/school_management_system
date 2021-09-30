from django import forms
from courses.models.course.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'code', 'department', 'is_active')
