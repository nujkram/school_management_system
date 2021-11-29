from django import forms
from activities.models.activity.models import Activity


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
