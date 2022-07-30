from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
class UserInfo(User):
    age=models.IntegerField()
    gender=models.CharField(max_length=7)
    contact=models.CharField(max_length=15)

    class Meta:
        db_table="userinfo"