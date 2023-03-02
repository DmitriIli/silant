from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from django.core.validators import EmailValidator

class SignupForm(UserCreationForm): 
    email = forms.EmailField(max_length=200, help_text='Required') 
    class Meta: 
        model = User 
        fields =('username', 'email',) 

# class RegisterForm(forms.Form):
#     username = forms.CharField(label='ФИО', max_length=64)
#     email = forms.EmailField(label='email', validators=EmailValidator)