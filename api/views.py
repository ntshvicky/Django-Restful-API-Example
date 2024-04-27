from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #companies/{company_id}/employees/
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            employee = Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializer(employee, many=True,context={'request': request})
            return Response(emp_serializer.data)
        except Company.DoesNotExist:
            return Response(status=404)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer