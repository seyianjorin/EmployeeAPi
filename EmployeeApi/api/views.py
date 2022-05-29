from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from EmployeeApiApp.models import Employee
from api.serializers import EmployeeSerializer
# Create your views here.


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [IsAuthenticated]
