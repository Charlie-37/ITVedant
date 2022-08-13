from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_user(request):
    if request.method == "POST":
        f = UserCreationForm(request.POST)
        f.save()
        return redirect('/')
    else:
        context = {'form':UserCreationForm,'fmsg':"UserForm"}
        return render(request,'form.html',context)



def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passw = request.POST.get('passw')
        user = authenticate(request,username=uname,password=passw)

        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('/')

    else:
        return render(request,'login.html')



def logout_view(request):
    logout(request)
    return redirect('/')