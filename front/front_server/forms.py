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


class SongCreationForm(forms.Form):
    url = forms.URLField(label='URL', required=True)
    title = forms.CharField(label='Title', max_length=64, required=True)
    author = forms.CharField(label='Author', max_length=64, required=True)
    source = forms.CharField(label='Source', max_length=64, required=True)
    start_point = forms.IntegerField(
        label='Start point', min_value=0, initial=0)
    length = forms.IntegerField(label='End point', min_value=20, initial=60)

    def clean(self):
        cleaned_data = super(SongCreationForm, self).clean()
        start_point = cleaned_data.get('start_point')
        length = cleaned_data.get('length')

        if start_point + 20 > length:
            self.add_error('length', 'Length too small')

        return cleaned_data
