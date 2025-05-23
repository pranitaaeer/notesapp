from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomeUser
        fields=['username','email']