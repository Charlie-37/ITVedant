from dataclasses import fields
from django import forms
from .models import Emp

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields="__all__"

class EmpForm1(forms.ModelForm):
    class Meta:
        model=Emp
        fields=['name','email']