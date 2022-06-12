from pyexpat import model
from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=15)
