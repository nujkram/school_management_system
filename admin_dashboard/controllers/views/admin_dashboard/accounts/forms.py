from django import forms
from accounts.models.account.models import Account
from django.contrib.auth.forms import UserCreationForm


class AccountForm(UserCreationForm):
    class Meta:
        model = Account
        fields = (
            "username",
            "email",
            "user_type"
        )
