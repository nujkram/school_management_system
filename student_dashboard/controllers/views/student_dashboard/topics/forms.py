from django import forms
from topics.models.topic.models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
