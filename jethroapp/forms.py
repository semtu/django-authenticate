from django import forms
from .models import form_model,user_model
from django.contrib.auth.models import User

class model_form(forms.ModelForm):
    class Meta:
        model=form_model
        fields='__all__'

class user_form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name','email','password',)

class profile_form(forms.ModelForm):
    class Meta:
        model=user_model
        fields=('portfolio','profile_pic',)

