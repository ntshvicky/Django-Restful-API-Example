from django.db import models

# Create your models here.


# create company model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'), 
                                                     ('Non-IT', 'Non-IT'), 
                                                     ('Other', 'Other')))
    added_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    deleted_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    dob = models.DateField()
    position = models.CharField(max_length=100, choices=(('CEO', 'CEO'), ('Manager', 'Manager'), ('Engineer', 'Engineer'), ('Intern', 'Intern')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    