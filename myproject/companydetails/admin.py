from django.contrib import admin

# Register your models here.
from companydetails.models import CompanyEmployee, Candidate

admin.site.register(CompanyEmployee)
admin.site.register(Candidate)