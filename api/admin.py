from django.contrib import admin

from api.models import Company, Employee

# modify API view
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'name', 'location', 'about', 'type', 'added_date', 'updated_date', 'deleted_date', 'active')
    list_editable = ('active',)
    list_filter = ('active',)
    search_fields = ('name', 'location', 'about', 'type')
    ordering = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'email', 'dob', 'position', 'company')
    list_filter = ('company',)
    search_fields = ('name', 'email', 'position', 'company')
    ordering = ('name',)


# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)