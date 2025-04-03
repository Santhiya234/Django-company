from rest_framework import serializers
from companydetails.models import CompanyEmployee, AccessEmployee, Candidate, CandidateSkill

class CompanyEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyEmployee
        fields = ['id', 'username', 'designation', 'department']            

class AccessEmployeeSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=CompanyEmployee.objects.all())

    class Meta:
        model = AccessEmployee
        fields = ['id', 'employee', 'role']
        
class CandidateSkillSerializer(serializers.ModelSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())

    class Meta:
        model = CandidateSkill
        fields = ['id', 'candidate', 'skill_name', 'skill_level']
        
class CandidateSerializer(serializers.ModelSerializer):
    skills = CandidateSkillSerializer(many=True, read_only=True)
    assigned_hr = CompanyEmployeeSerializer(read_only=True)

    class Meta:
        model = Candidate
        fields = ['id', 'name', 'email', 'phone', 'applied_position', 'skills', 'assigned_hr']

class HRAssignedCandidateSerializer(serializers.ModelSerializer):
    assigned_candidates = CandidateSerializer(many=True, read_only=True)
    
    class Meta:
        model = CompanyEmployee
        fields = ['id', 'username', 'designation', 'assigned_candidates']
       