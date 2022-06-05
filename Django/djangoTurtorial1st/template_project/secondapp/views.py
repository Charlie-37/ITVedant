from django.shortcuts import render

# Create your views here.
def sec(request):
    return render(request, "second.html")
    