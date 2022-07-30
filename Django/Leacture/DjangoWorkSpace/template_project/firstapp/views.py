from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,"home.html")

def first_call(request):
    return render(request,"fst.html")


def second_call(request):
    return render(request,"sc.html")