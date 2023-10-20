from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Feedback, Contact_us

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class FeebackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['username', 'feedback']
    

class Contact_usForm(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = '__all__'