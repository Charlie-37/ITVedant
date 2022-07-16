from dataclasses import field, fields
from django import forms

from django.contrib.auth.models import User


class UserForm1(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserForm2(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username",'password','email']


from django.contrib.auth.forms import UserCreationForm
class UserForm4(UserCreationForm):
    class Meta:
        model = User
        fields = ["username",'first_name','email','last_name','password1','password2']