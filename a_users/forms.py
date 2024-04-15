from django.forms import ModelForm
from django import forms
from .models import CustomUser

class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'ages', 'gender']
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'What is your name?'}),
            'ages' : forms.RadioSelect(),
            'gender' : forms.RadioSelect()
        }