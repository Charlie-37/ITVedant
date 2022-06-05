from django.shortcuts import redirect, render,redirect

# Create your views here.

def homePage(request):
    return render(request, "home.html")

def home(request):
    return redirect('/')