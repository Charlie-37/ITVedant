
from django.contrib import admin
from django.urls import path
from firstapp.views import home
from firstapp import views as v
from thirdapp import views as tv
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('app1_first',v.first_call),
    path('app1_second',v.second_call),
    path('app3_first',tv.third_call),
     path('app3_second',tv.fourth_call),
    
]
