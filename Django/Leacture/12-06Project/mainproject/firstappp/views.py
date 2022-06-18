from tkinter import E
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

# //*---- Saving DATA TO THE MYSQL LITE3 BY DIRECT LOADING THE FORM

from .forms import EmpForm
def EmpForm2(request):
    
    if request.method == 'POST':
        f = EmpForm(request.POST)
        f.save()


        return redirect('/')
    else:
        d = {"form" : EmpForm}
        return render(request, 'fempForm2.html', d)

#//*-----SHOW ALL USER LIST---*//
def UserList(request):
    ul = Emp.objects.all()
    d = {'ul': ul}
    return render(request,'userList.html',d)


#//*----DELETE EMP BY GIVING KEY PAIR
def delete_emp(request):
    eid = request.GET.get('id')
    emp = Emp.objects.get(id=eid)
    emp.delete()
    return redirect("/")

# //*----Delete EMP BY DIRECT ID
def delete_emp2(request,id):
    emp = Emp.objects.get(id=id)
    emp.delete()
    return redirect("/userList")


# //*------UPDATE EMP FORM
def edit_emp(request,id):
    emp = Emp.objects.get(id=id)

    if request.method == 'POST':
        f = EmpForm(request.POST,instance=emp)
        f.save()
        return redirect('/userList')

    else:
        f = EmpForm(instance=emp)
        context = {'form':f}
        return render(request,'fempForm2.html',context)