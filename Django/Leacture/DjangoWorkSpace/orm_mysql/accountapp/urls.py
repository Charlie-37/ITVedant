
from django.urls import path
from .import views as v
urlpatterns = [
    path("adduser1",v.add_user1),
    path("adduser2",v.add_user2),
    path("adduser3",v.add_user3),
    path("adduser4",v.add_user4),
    path("adduser5",v.add_user5),
    path("login",v.login_view),
    path("logout",v.logout_view),
]
