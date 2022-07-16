from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(User):
    age = models.ImageField()
    gender = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)

    class Meta:
        db_table = 'userinfo'