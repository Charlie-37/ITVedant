
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from restapp.views import CRUDUser1,CRUDUser2,CRUDACC,CRUDProject
rt=routers.DefaultRouter()
rt.register('user1',CRUDUser1)
rt.register('user2',CRUDUser2)
rt.register('acc',CRUDACC)
rt.register('prj',CRUDProject)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('restapp.urls')),
    path('',include(rt.urls)),
]
