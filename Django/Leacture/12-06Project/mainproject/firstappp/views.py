from django.shortcuts import redirect, render

from firstappp.models import Emp

# Create your views here.

def home(request):
    return render(request,'home.html')

def EmpForm(request):

    if request.method == 'POST':
        e = Emp()
        e.name = request.POST.get('emp_name')
        e.email = request.POST.get('emp_email')
        e.contact = request.POST.get('emp_contact')
        e.save()
        return redirect('/')
    else:
        return render(request, 'empForm.html')


def insertData(request):
    e = Emp()
    e.name='Sagar'
    e.email='Sagar123@gmail.com'
    e.contact=89165425
    e.save()

    return redirect('/')

from .forms import EmpForm
def EmpForm2(request):
    
    if request.method == 'POST':
        f = EmpForm(request.POST)
        f.save()


        return redirect('/')
    else:
        d = {"form" : EmpForm}
        return render(request, 'fempForm2.html', d)


def UserList(request):
    ul = Emp.objects.all()
    d = {'ul': ul}
    return render(request,'userList.html',d)