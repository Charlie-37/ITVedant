import email
from django.shortcuts import render,redirect

from ormapp.models import Emp

def home(request):
    return render(request,'home.html')

def insert1(request):
    e=Emp()
    e.name="Sagar"
    e.email="s@gmail.com"
    e.contact=8855522
    e.save()
    return redirect("/")

def insert2(request):
    if request.method=="POST":
        e=Emp()
        e.name=request.POST.get("name")
        e.email=request.POST.get("email")
        e.contact=request.POST.get("contact")
        e.save()
        return redirect("/")
    else:
        return render(request,"adduser.html")

from .forms import EmpForm,EmpForm1
def insert3(request):
    if request.method=="POST":
        f=EmpForm(request.POST)
        f.save()


        return redirect("/")
    else:

        d={'form':EmpForm}
        return render(request,"adduser2.html",d)

def insert4(request):
    if request.method=="POST":
        f=EmpForm1(request.POST)
        f.save()
        return redirect("/")
    else:

        d={'form':EmpForm1}
        return render(request,"adduser2.html",d)

def user_list(request):
    ul=Emp.objects.all()
    d={'ul':ul}
    return render(request,"userlist.html",d)

def emp_delete(request):
    eid=request.GET.get("id")
    emp=Emp.objects.get(id=eid)
    emp.delete()
    return redirect("/ulist")

def emp_delete2(request,id):
    emp=Emp.objects.get(id=id)
    emp.delete()
    return redirect("/ulist")

def emp_edit(request,id):
    emp=Emp.objects.get(id=id)
    if request.method=='POST':
        f=EmpForm(request.POST,instance=emp)
        f.save()
        return redirect("/ulist")
    else:
        f=EmpForm(instance=emp)
        context={"form":f}
        return render(request,"adduser2.html",context)