from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from .import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.home),
    path('insert', v1.insertData),
    path('EmpData', v1.EmpForm),
    path('EmpData2', v1.EmpForm2),
    path('userList', v1.UserList),
    path('delete_emp', v1.delete_emp),
    path('delete_emp2/<int:id>', v1.delete_emp2),
    path('edit_emp/<int:id>', v1.edit_emp),
    ]
