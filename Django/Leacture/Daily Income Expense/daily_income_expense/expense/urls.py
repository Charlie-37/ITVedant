
from django.contrib import admin
from django.urls import path

from .import views as v

urlpatterns = [
    path('add',v.add_expense,name='add'),
    path('list',v.expense_list,name='elist'),
]
