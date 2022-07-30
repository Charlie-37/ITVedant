
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('empapp.urls')),
    path('',include('accountapp.urls')),
    path('',include('practiceapp.urls')),
]
