from django import forms
from profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'company',
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'gender',
            'contact_number',
            'address',
            'country',
            'region',
            'province',
            'city',
            'zip_code',
        )

    class Media:
        js = ('common/js/gijgo.min.js',)
        css = {
            'all': ('common/css/gijgo.min.css',)
        }
