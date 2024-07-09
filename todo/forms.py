from django.forms import ModelForm
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class Taskform(ModelForm):
    class Meta:
        model=Task
        fields='__all__'

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)  
    email = forms.EmailField(label='email')  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput) 
                

        