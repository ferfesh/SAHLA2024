
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Member

class MemberRegistrationForm(UserCreationForm):
    national_id = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(max_length=255)
    upline_name = forms.CharField(max_length=255)
    upline_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'national_id', 'phone', 'email', 'address', 'upline_name', 'upline_number']
