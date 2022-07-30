
from dataclasses import fields
import imp
from  rest_framework import serializers
from .models import Emp,Account,Project
from django.contrib.auth.models import User

class EmpSerializer(serializers.ModelSerializer):
    emp_acc=serializers.PrimaryKeyRelatedField(many=True, queryset=Account.objects.all())
    emp_wp=serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())

    class Meta:
        model=Emp
        fields=['id','name','email','contact','age','emp_acc','emp_wp']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','first_name','last_name']


class UserSerializer2(serializers.HyperlinkedModelSerializer):
    user_project=serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())

    class Meta:
        model=User
        fields=['url','username','email','first_name','last_name','user_project']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields='__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'
