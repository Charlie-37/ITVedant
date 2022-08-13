
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('add',v.add_income,name='add'),
    path('list',v.income_list,name='ilist')

]
