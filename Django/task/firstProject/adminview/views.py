# from crypt import methods
from django.shortcuts import redirect, render

dataList = []
# Create your views here.
def adminLogin(request):
    return render(request,'adminLogin.html')

def adminRegister(request):

    if request.method == "POST":
        
        id = request.POST.get('admin_id')
        username = request.POST.get('admin_name')
        user_email = request.POST.get('admin_email')
        user_contact = request.POST.get('admin_contact')


        t = (id,username,user_email,user_contact)

        dataList.append(t)

        return redirect('/')
    else:
        return render(request, 'adminRegister.html')

def adminList(request):
    admin_data = {'ul' : dataList}
    print(dataList)
    return render(request, 'adminList.html', admin_data)