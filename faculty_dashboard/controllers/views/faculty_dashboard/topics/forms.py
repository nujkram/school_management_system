from django import forms
from topics.models.topic.models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = (
            'name',
            'description',
            'academic_year_subject',
            'subject',
        )

    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        self.fields['academic_year_subject'].widget.attrs['readonly'] = True
        self.fields['subject'].widget.attrs['readonly'] = True
