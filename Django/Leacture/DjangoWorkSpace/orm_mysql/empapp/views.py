import imp
from django.shortcuts import render,redirect
from .forms import Emp,EmpForm,EmpQuali,EmpQualiForm,EmpQualiForm2,EmpQuali2
# Create your views here.

def home(request):
    return render(request,"home.html")

def addemp(request):
    if request.method=='POST':
        f=EmpForm(request.POST)
        f.save()
        return redirect("/")
    else:
        context={'form':EmpForm}
        return render(request,"form.html",context)

def add_qualif(request):
    if request.method=='POST':
        f=EmpQualiForm(request.POST)
        f.save()
        return redirect("/")
    else:
        context={'form':EmpQualiForm}
        return render(request,"form.html",context)

def emp_qualif_list(request):
    eq=EmpQuali.objects.all()
    return render(request,"empqlist.html",{'eqlist':eq})

def add_qualif2(request):
    if request.method=='POST':
        f=EmpQualiForm2(request.POST)
        f.save()
        return redirect("/")
    else:
        context={'form':EmpQualiForm2}
        return render(request,"form.html",context)

def emp_qualif_list2(request):
    eq=EmpQuali2.objects.all()
    return render(request,"empqlist2.html",{'eqlist':eq})

from .forms import EmpQuali3,EmpQualiForm3
def add_qualif3(request):
    if request.method=='POST':
        f=EmpQualiForm3(request.POST)
        f.save()
        return redirect("/")
    else:
        context={'form':EmpQualiForm3}
        return render(request,"form.html",context)

from .forms import Singer,SingerForm,Songs,SongsForm
def add_singer(request):
    if request.method=='POST':
        f=SingerForm(request.POST)
        f.save()
        return redirect("/")
    else:
        context={'form':SingerForm}
        return render(request,"form.html",context)


def add_songs(request):
    if request.method=='POST':
        f=SongsForm(request.POST)
        f.save()
        return redirect("/")
    else:
        context={'form':SongsForm}
        return render(request,"form.html",context)
