from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from .import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.home),
    path('insert', v1.insertData),
    path('EmpData', v1.EmpForm)
    ]