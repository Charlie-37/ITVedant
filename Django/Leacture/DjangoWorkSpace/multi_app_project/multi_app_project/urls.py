
from django.contrib import admin
from django.urls import path,include
from firstapp import views as v
from secondapp import views as sv
from thirdapp import views as tv

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',v.home),
    path('',include('firstapp.urls')),
    path('',include('secondapp.urls')),
    
]
