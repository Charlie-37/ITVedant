from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
from .models import Income, IncomeForm

def add_income(request):
    if request.method == 'POST':
        income = request.POST.get('income')
        incomeType = request.POST.get('incomeType')
        description = request.POST.get('description')
        user = User.objects.get(id=request.session.get('uid'))
        i = Income()
        i.income = income
        i.incomeType = incomeType
        i.user = user
        i.description = description
        i.save()
        return redirect('/')
    else:
        context = {'form':IncomeForm,'fmsg':"Income Form"}
        return render(request,'form.html',context)


def income_list(request):
    uid = request.session.get('uid')
    incl = Income.objects.filter(user=uid)
    context = {'incl':incl}
    return render(request,'inclist.html',context)
