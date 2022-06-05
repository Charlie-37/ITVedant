
from django.contrib import admin
from django.urls import path, include
from firstapp import views as v
from secondapp import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),


    path('home',v.home),
    path('',include('firstapp.urls')),
    path('',include('secondapp.urls')),
    path('',include('thirdapp.urls')),
]
