from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializer import Employeeserializer
from .pagination import Mypagination
from .models import Employee
# Create your views here.



class EmployeeInfo(ListAPIView):
    serializer_class = Employeeserializer
    queryset = Employee.objects.all()
    pagination_class = Mypagination
