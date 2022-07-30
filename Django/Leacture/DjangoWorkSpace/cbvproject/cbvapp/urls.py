
from .import views as v
from django.urls import path
from django.views.generic import TemplateView
urlpatterns = [
   path('',TemplateView.as_view(template_name="home.html")),
   path('demo',v.Demo.as_view()),
   path('reg',v.EmpRegisterForm.as_view()),
   path('saveemp',v.CreateEmp.as_view()),
   path('regDemo',v.Register.as_view()),
   path('save',v.RegisterForm.as_view()),
   path('emplist',v.EmpListView.as_view()),
   path('d1/<int:pk>',v.DeletEmp1.as_view()),
   path('d2/<int:pk>',v.DeletEmp2.as_view()),
   path('e/<int:pk>',v.UpdateEmpView.as_view()),
   
]
 