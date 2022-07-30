from django.shortcuts import render

def first_url(request):
    return render(request,'first.html')

def home(request):
    return render(request,'home.html')