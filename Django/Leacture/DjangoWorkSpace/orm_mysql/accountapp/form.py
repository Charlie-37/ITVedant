from dataclasses import fields
import imp
from django import forms

from django.contrib.auth.models import User

class UserForm1(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

class UserForm2(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name',"last_name","user_permissions","email",'password']

from django.contrib.auth.forms import UserCreationForm
class UserForm4(UserCreationForm):
    class Meta:
        model=User
        fields=["username",'first_name','last_name',"email",'password1','password2']

from .models import UserInfo
class UserForm5(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=["username",'first_name','last_name','age','gender',"email",'contact','password1','password2']