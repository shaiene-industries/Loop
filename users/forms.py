from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150, required=True)
    password = forms.CharField(label="Password", max_length=128, required=True, widget=forms.PasswordInput)
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput()
        }
        fields = ['username','password']