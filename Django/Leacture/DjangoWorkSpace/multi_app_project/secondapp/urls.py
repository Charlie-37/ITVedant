

from django.urls import path
from .import views as v
urlpatterns = [
   path('sec',v.second_url),
   path('register',v.register),
   path('addfirst',v.adduser1),
   path('addsec',v.adduser2),
   path('register2',v.register2),
   path("userlist",v.user_list),
]
