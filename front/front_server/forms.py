from django import forms
from django.forms.widgets import PasswordInput


class LoginForm(forms.Form):
    login = forms.CharField(label='Login', max_length=32)
    password = forms.CharField(widget=forms.PasswordInput())


class RegistrationForm(forms.Form):
    login = forms.CharField(label='Login', max_length=32)
    password = forms.CharField(widget=forms.PasswordInput())
    confirmPassword = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirmPassword = cleaned_data.get("confirmPassword")

        if password != confirmPassword:
            self.add_error('confirmPassword', "Password does not match")

        return cleaned_data


class LobbyCreationForm(forms.Form):
    titleWeight = forms.FloatField(label='Title Weight', initial=0.5)
    authorWeight = forms.FloatField(label='Author Weight', initial=0.5)
    sourceWeight = forms.FloatField(label='Source Weight', initial=0)

    def clean(self):
        cleaned_data = super(LobbyCreationForm, self).clean()
        titleWeight = cleaned_data.get('titleWeight')
        authorWeight = cleaned_data.get('authorWeight')
        sourceWeight = cleaned_data.get('sourceWeight')

        if titleWeight < 0:
            self.add_error('titleWeight', 'Negative title weight')

        if authorWeight < 0:
            self.add_error('authorWeight', 'Negative author weight')

        if sourceWeight < 0:
            self.add_error('sourceWeight', 'Negative source weight')

        if (titleWeight + authorWeight + sourceWeight != 1):
            self.add_error('titleWeight', 'Weights do not sum up to 1')

        return cleaned_data
