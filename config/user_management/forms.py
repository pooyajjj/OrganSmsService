from collections import UserList
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    gender = forms.CharField()
    birthday = forms.CharField()
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'gender', 'birthday']