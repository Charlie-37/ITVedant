
from django.contrib import admin
from .import views as v
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html")),
    path('demo',v.Demo.as_view()),
    path('reg',v.EmpRegisterForm.as_view()),
    path('saveemp',v.CreateEmp.as_view()),
    path('emplist',v.EmpListView.as_view()),
    path('d1/<int:pk>',v.DeleteEmp1.as_view()),
    path('e/<int:pk>',v.UpdateEmpView.as_view()),

]
