from django import forms
from activity_files.models.activity_file.models import ActivityFile


class ActivityFileForm(forms.ModelForm):
    class Meta:
        model = ActivityFile
        fields = (
            'attached_file',
        )
