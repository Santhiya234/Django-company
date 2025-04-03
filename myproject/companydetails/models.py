from django.db import models
from django.contrib.auth.models import AbstractUser

class CompanyEmployee(AbstractUser):
    designation = models.CharField(max_length=150)
    department = models.CharField(max_length=150)

    groups = None
    user_permissions = None

    def __str__(self):
        return self.username

class AccessEmployee(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('HR', 'HR'),
    ]
    employee = models.OneToOneField(CompanyEmployee, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.employee.username} - {self.role}"

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    applied_position = models.CharField(max_length=100) 
    assigned_hr = models.ForeignKey(CompanyEmployee, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_candidates")

    def __str__(self):
        return self.name  

class CandidateSkill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=50)  # Basic, Intermediate, Advanced

    def __str__(self):
        return f"{self.candidate.name} - {self.skill_name}"



# class CandidateAssigntoHR(models.Model):
#     candidate = models.models.OneToOneField("Candidate", on_delete=models.CASCADE)
    