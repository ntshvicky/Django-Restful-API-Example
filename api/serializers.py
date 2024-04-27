from api.models import Company, Employee
from rest_framework import serializers


# create serialzers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = '__all__'
        #fields = ('company_id', 'name', 'location', 'about', 'type', 'added_date', 'updated_date', 'deleted_date', 'active')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = '__all__'
        #fields = ('employee_id', 'name', 'email', 'dob', 'position', 'company', 'added_date', 'updated_date', 'deleted_date', 'active')
        