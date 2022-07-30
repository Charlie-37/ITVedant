from django.shortcuts import render,HttpResponse
from rest_framework import generics as g
from .serializer import Emp,EmpSerializer
def home(request):
    return HttpResponse("<h1> Django rest project </h1>")


class AddEmp(g.CreateAPIView):
    queryset=Emp
    serializer_class=EmpSerializer

class EmpList(g.ListAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class CreateListEmp(g.ListCreateAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class DeleteEmp(g.DestroyAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class UpdateEmp(g.UpdateAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class GetEmp(g.RetrieveAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class GUEmp(g.RetrieveUpdateAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class GDEmp(g.RetrieveDestroyAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class GUDEmp(g.RetrieveUpdateDestroyAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

from .serializer import UserSerializer,User,UserSerializer2,Account,AccountSerializer,Project,ProjectSerializer

class CLUser(g.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class GUDUser(g.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

from rest_framework.viewsets import ModelViewSet

class CRUDUser1(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class CRUDUser2(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer2

class CRUDACC(ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer

class CRUDProject(ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer