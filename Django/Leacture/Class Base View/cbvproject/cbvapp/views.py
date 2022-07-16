
from pyexpat import model
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView,DeleteView,UpdateView,ListView
from django.views.generic.edit import CreateView
from .models import Emp, EmpForm

class Demo(TemplateView):
    template_name = "demo.html"

class EmpRegisterForm(FormView):
    form_class= EmpForm
    template_name = "form.html"


class CreateEmp(CreateView):
    model = Emp
    fields = '__all__'
    success_url="/"
# Create your views here.

class Register(FormView,CreateView):
    form_class=EmpForm
    template_name = "addemp.html"

class EmpListView(ListView):
    model=Emp
    template_name = "emplist.html"

class DeleteEmp1(DeleteView):
    model = Emp
    template_name = "delete.html"
    success_url = "/"

class UpdateEmpView(UpdateView):
    template_name = "updateemp.html"
    model = Emp
    fields = "__all__"
    success_url = "/emplist"