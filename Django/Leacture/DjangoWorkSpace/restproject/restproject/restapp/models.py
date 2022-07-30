from django.db import models
from django.contrib.auth.models import User
class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    age=models.CharField(max_length=30)
    

class Account(models.Model):
    salary=models.IntegerField()
    month=models.CharField(max_length=30)
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE,related_name="emp_acc")


class Project(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_project')
    emp=models.ManyToManyField(Emp,related_name='emp_wp')