# forms.py
from django import forms
from django.contrib.auth.forms import PasswordResetForm

class PasswordResetRequestForm(PasswordResetForm):
    email = forms.EmailField(
        label="Enter your email",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control'
        })
    )