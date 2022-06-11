from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')
# Create your views here.

def AboutUs(request):
    return render(request, 'aboutUs.html')

