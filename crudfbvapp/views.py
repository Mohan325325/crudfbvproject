from django.shortcuts import render,redirect
from . forms import EmployeeForm
from .models import EmployeeModel

# Create your views here.
def insert_view(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm()
    return render(request,'crudfbvapp/insert.html',{'form':form})

def retriew_view(request):
    employees = EmployeeModel.objects.all()
    return render(request,'crudfbvapp/home.html',{'employees':employees})

def delete_view(request,id):
    employee = EmployeeModel.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    employee = EmployeeModel.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'crudfbvapp/update.html',{'employee':employee})
