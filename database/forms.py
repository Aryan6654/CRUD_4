from django import forms
from django.forms import fields, widgets
from django.core import validators
from .models import User

class EmployeeRegistrations(forms.ModelForm):
    class Meta:
        model = User
        fields =['name', 'email', 'address']
        widgets = {
            'name': forms.TextInput,
            'email': forms.EmailInput,
            'address': forms.TextInput,
        }
