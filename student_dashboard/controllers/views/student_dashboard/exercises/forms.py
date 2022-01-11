from django import forms
from exercises.models.exercise.models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = (
            'name', 'attached_file', 'remarks', 'activity'
        )
        widgets = {
            'activity': forms.TextInput(attrs={'class': 'custom-file-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        self.fields['activity'].widget.attrs['readonly'] = True
