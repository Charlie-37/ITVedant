from django.shortcuts import render

def third_call(request):
    return render(request,"thr.html")

def fourth_call(request):
    return render(request,"fr.html")