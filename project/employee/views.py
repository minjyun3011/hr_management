from django.views import generic
from .models import Employee

class IndexView(generic.ListView):
    model=Employee
    template_name = 'employee/employee_list.html' 
