from django.shortcuts import render,HttpResponse
from rest_framework import generics as g
from .serialize import Emp, EmpSerialize

def home(request):
    return HttpResponse("<h1>Django Rest Framework</h1>")


class AddEmp(g.CreateAPIView):
    queryset=Emp
    serializer_class=EmpSerialize


class EmpList(g.ListAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerialize

class CreateListEmp(g.ListCreateAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerialize

# Create your views here.
