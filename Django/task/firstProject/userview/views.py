from django.shortcuts import redirect, render

# Create your views here.

def userLogin(request):
    return render(request, 'userLogin.html')

def UserRegister(request):
    return render(request, 'userRegister.html')

def addUser(request):
    id = request.POST.get('user_id')
    username = request.POST.get('user_name')
    user_email = request.POST.get('user_email')
    user_contact = request.POST.get('user_contact')

    print(id,username,user_email,user_contact)
    return redirect('/')