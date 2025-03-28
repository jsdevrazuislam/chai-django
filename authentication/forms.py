from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):

    input_style = 'w-full p-2 border border-gray-300 rounded-lg focus:ring focus:ring-blue-200 text-black'

    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': input_style,
        'placeholder': 'Enter your first_name'
    }))

    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': input_style,
        'placeholder': 'Enter your last_name'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': input_style,
        'placeholder': 'Enter username'
    }))
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': input_style,
        'placeholder': 'Enter your email'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': input_style,
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': input_style,
    }))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
