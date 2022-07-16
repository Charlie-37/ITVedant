from dataclasses import field
from django.db import models

# Create your models here.

class Emp(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    contact = models.CharField(max_length=20)
    age = models.CharField(max_length=10)
    description = models.TextField(max_length=300)


from django import forms

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields = "__all__"

