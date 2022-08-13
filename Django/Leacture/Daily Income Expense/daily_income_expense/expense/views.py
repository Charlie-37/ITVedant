from django.shortcuts import render,redirect

# Create your views here.
from .models import Expense,ExpenseForm
from django.contrib.auth.models import User

def add_expense(request):
    if request.method == 'POST':
        expense = request.POST.get('expense')
        expense_Type = request.POST.get('expense_Type')
        description = request.POST.get('description')
        user = User.objects.get(id=request.session.get('uid'))
        i = Expense()
        i.expense = expense
        i.expense_Type = expense_Type
        i.user = user
        i.description = description
        i.save()
        return redirect('/')
    else:
        context = {'form':ExpenseForm,'fmsg':"Expense Form"}
        return render(request,'form.html',context)


def expense_list(request):
    context = {'expl':Expense.objects.all()}
    return render(request,'explist.html',context)