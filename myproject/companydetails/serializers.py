from rest_framework import serializers
from companydetails.models import CompanyEmployee,AccessEmployee,Candidate,CandidateSkill

class CompanyEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyEmployee
        fields = "__all__"
        
class AccessEmployeeSerializer(serializers.ModelSerializer):
    employee = CompanyEmployeeSerializer()
    
    class Meta:
        models = AccessEmployee
        fields = ['id', 'employee', 'role']
        
class CandidateSkillSerializer(serializers.ModelSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())

    class Meta:
        model = CandidateSkill
        fields = ['id', 'candidate', 'skill_name', 'skill_level']
        
class CandidateSerializer(serializers.ModelSerializer):
    skills = CandidateSkillSerializer(many=True, read_only=True)
    class Meta:
        model = Candidate
        fields = '__all__'