from pyexpat import model
from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Std(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,primary_key=True)
    address=models.TextField(max_length=300)

    class Meta:
        db_table="student"
