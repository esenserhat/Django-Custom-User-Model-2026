from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, UserChangeForm, PasswordChangeForm
from .models import Account

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'E-mail',
                'class':'eo-form-input'
            }
        )
    )

    password = forms.CharField(
        label='', 
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'Password',
                'class':'eo-form-input',
            }
        )
    )


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'eo-form-input',
        'placeholder': 'Email',
        'type': 'text',
        'name': 'email'
        }))


class UserSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserSetPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label='', widget=forms.EmailInput(attrs={
        'class': 'eo-form-input',
        'placeholder': 'New Password',
        'type': 'password',
        'name': 'password'
        }))
    new_password2 = forms.CharField(label='', widget=forms.EmailInput(attrs={
        'class': 'eo-form-input',
        'placeholder': 'Repeat New Password',
        'type': 'password',
        'name': 'confirm_password'
        }))
    

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    old_password = forms.CharField(label='', widget=forms.EmailInput(attrs={
        'class': 'eo-form-input',
        'placeholder': 'Current Password',
        'type': 'password',
        'name': 'password'
        }))
    new_password1 = forms.CharField(label='', widget=forms.EmailInput(attrs={
        'class': 'eo-form-input',
        'placeholder': 'New Password',
        'type': 'password',
        'name': 'password'
        }))

    new_password2 = forms.CharField(label='', widget=forms.EmailInput(attrs={
        'class': 'eo-form-input',
        'placeholder': 'Repeat New Password',
        'type': 'password',
        'name': 'confirm_password'
        }))