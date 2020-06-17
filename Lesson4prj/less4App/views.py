from django.shortcuts import render
from .models import Employee
# Create your views here.
def index(request):
    emp = Employee.objects.all()
    context = {'title': 'Welcome', 'employees': emp}
    return render(request, 'index.html', context)
