from dataclasses import fields
import imp
from pyexpat import model
from django import forms

from .models import Emp

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'