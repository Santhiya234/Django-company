from rest_framework import serializers
from companydetails.models import CompanyEmployee, AccessEmployee, Candidate, CandidateSkill


class AccessEmployeeSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=CompanyEmployee.objects.all())

    class Meta:
        model = AccessEmployee
        fields = ['employee', 'role']
        
class CompanyEmployeeSerializer(serializers.ModelSerializer):
    roles = AccessEmployeeSerializer(many=True, read_only=True, source="access_role")
    
    class Meta:
        model = CompanyEmployee
        fields = ['id', 'username', 'designation', 'department', 'roles', 'photo'] 

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
    assigned_candidates = CandidateSerializer(many=True, read_only=True, source="assigned_candidates")
    
    class Meta:
        model = CompanyEmployee
        fields = ['id', 'username', 'designation', 'assigned_candidates']





       