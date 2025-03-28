from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring focus:ring-blue-200 text-black'
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring focus:ring-blue-200 text-black'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring focus:ring-blue-200 text-black'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring focus:ring-blue-200 text-black'
    }))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
