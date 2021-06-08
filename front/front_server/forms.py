from django import forms
from django.forms.widgets import PasswordInput


class LoginForm(forms.Form):
    login = forms.CharField(label='Login', max_length=32)
    password = forms.CharField(widget=forms.PasswordInput())


class RegistrationForm(forms.Form):
    login = forms.CharField(label='Login', max_length=32)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data
