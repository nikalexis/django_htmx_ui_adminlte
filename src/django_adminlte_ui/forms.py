from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'id': 'email',
                                                            'class': "form-control",
                                                            'placeholder': 'Email'}),
                             required=True)
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'id':'password',
                                                                 'class': "form-control",
                                                                 'placeholder': 'Password'}),
                               min_length=4,
                               required=True)
    confirm_password = forms.CharField(label='',
                                       widget=forms.PasswordInput(attrs={'id': 'confirm_password',
                                                                         'class': "form-control",
                                                                         'placeholder': 'Confirm password'}),
                                       min_length=4,
                                       required=True)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('password', 'Passwords do not match.')
            return

        if len(User.objects.filter(username=email)) > 0:
            self.add_error('email', 'There is already an account with this email.')
            return

        return self.cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'id': 'email',
                                                            'class': "form-control",
                                                            'placeholder': 'Email'}),
                             required=True)
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'id': 'password',
                                                                 'class': "form-control",
                                                                 'placeholder': 'Password'}),
                               min_length=4,
                               required=True)
