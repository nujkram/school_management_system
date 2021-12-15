from django import forms
from exercises.models.exercise.models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'
