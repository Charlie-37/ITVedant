from django.shortcuts import render,HttpResponse,redirect

datalist=[]
# Create your views here.
def second_url(request):
    return render(request,"second.html")

def third_url(request):
    return redirect('/first')

def register(request):
    return render(request,'adduser.html')

def adduser1(request):
    id=request.GET.get("id")
    n=request.GET.get("name")
    e=request.GET.get("email")
    c=request.GET.get("contact")
    print(id,n,e,c)
    return redirect("/")


def adduser2(request):
    id=request.POST.get("id")
    n=request.POST.get("name")
    e=request.POST.get("email")
    c=request.POST.get("contact")
    print(id,n,e,c)
    return redirect("/")

def register2(request):
    if request.method=='POST':
        id=request.POST.get("id")
        name=request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        t=(id,name,email,contact)
        datalist.append(t)
        print(datalist)
        return redirect("/")
    else:
        return render(request,'adduser2.html')

def user_list(request):
    d={"ul":datalist}
    return render(request,"ulist.html",d)