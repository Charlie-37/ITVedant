from django.shortcuts import render

# Create your views here.
def secondPage(request):
    return render(request,"second.html")