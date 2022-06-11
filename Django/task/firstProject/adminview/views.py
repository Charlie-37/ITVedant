from django.shortcuts import render

# Create your views here.
def adminLogin(request):
    return render(request,'adminLogin.html')

def adminRegister(request):
    return render(request, 'adminRegister.html')