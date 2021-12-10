from django import forms
from activities.models.activity.models import Activity


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = (
            'name',
            'description',
            'category',
            'video_url',
            'attached_file',
            'topic',
        )

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['topic'].widget.attrs['readonly'] = True
