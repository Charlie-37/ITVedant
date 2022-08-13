
from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    path('adduser',v.add_user,name='add'),
    path('login',v.login_view,name='ulogin'),
    path('logout',v.logout_view,name='ulogout'),
]
