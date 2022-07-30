
from django.contrib import admin
from django.urls import path
from .controller import first_call,second_call,home

urlpatterns = [
    path('admin/', admin.site.urls),	
    path('data',first_call),
    path('demo',second_call),
    path('',home),
]
