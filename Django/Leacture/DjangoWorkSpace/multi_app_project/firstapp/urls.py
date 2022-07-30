from django.urls import path

from .import views as v

urlpatterns = [
   path('first',v.first_url),
]
