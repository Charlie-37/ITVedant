
from django.contrib import admin
from django.urls import path
from .import views as v 
urlpatterns = [
    path('', v.home),
    path('addemp',v.AddEmp.as_view()),
    path('emplist',v.EmpList.as_view()),
    path('el',v.CreateListEmp.as_view()),
    path('demp/<int:pk>',v.DeleteEmp.as_view()),
    path('uemp/<int:pk>',v.UpdateEmp.as_view()),
    path('gemp/<int:pk>',v.GetEmp.as_view()),
    path('guemp/<int:pk>',v.GUEmp.as_view()),
    path('gdemp/<int:pk>',v.GDEmp.as_view()),
    path('gudemp/<int:pk>',v.GUDEmp.as_view()),
    path('cluser',v.CLUser.as_view()),
    path('guduser/<int:pk>',v.GUDUser.as_view()),
]
