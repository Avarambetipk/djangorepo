from django.shortcuts import render
from ormsapp.models import Employee
def retrieve_view(request):
    emp_list = Employee.objects.all()
    return render(request,'ormsapp/index.html',{'emp_list':emp_list})
