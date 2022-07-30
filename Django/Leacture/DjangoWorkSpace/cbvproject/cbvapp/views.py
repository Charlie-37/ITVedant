from django.views.generic import TemplateView,FormView,ListView,DeleteView,UpdateView
from django.views.generic.edit import CreateView
from .models import Emp,EmpForm


class Demo(TemplateView):
    template_name="demo.html"

class EmpRegisterForm(FormView):
    form_class=EmpForm
    template_name="form.html"

class CreateEmp(CreateView):
    model=Emp
    fields="__all__"
    success_url="/"
    
class Register(FormView,CreateView):
    form_class=EmpForm
   
    template_name="addemp.html"

class RegisterForm(CreateView):
    model=Emp
    fields='__all__'
    success_url="/"

class EmpListView(ListView):
    model=Emp
    template_name='emplist.html'

class DeletEmp1(DeleteView):
    model=Emp

    success_url="/"

class DeletEmp2(DeleteView):
    model=Emp
    template_name="delete.html"
    success_url="/emplist"

class UpdateEmpView(UpdateView):
    template_name="updateemp.html"
    model=Emp
    fields='__all__'
    success_url="/emplist"