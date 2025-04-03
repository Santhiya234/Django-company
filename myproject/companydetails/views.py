#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from companydetails.models import CompanyEmployee, Candidate, CandidateSkill
from companydetails.serializers import CompanyEmployeeSerializer, CandidateSkillSerializer, CandidateSerializer

class CompanyEmployeeListView(APIView):
    def get(self, request):
        employees = CompanyEmployee.objects.all()
        serializer = CompanyEmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanyEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CompanyEmployeeDetailView(APIView):
    def get(self, request, pk):
        employee = get_object_or_404(CompanyEmployee, pk=pk)
        serializer = CompanyEmployeeSerializer(employee)
        return Response(serializer.data)
    
    def put(self, request, pk):
        employee = get_object_or_404(CompanyEmployee, pk=pk)
        serializer = CompanyEmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        employee = get_object_or_404(CompanyEmployee, pk=pk)
        employee.delete()
        return Response()

class CandidateListView(APIView):
    def get(self, request):
        candidate = Candidate.objects.all()
        serializer = CandidateSerializer(candidate, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CandidateDetailAPIView(APIView):
    def get(self, request, pk):
        candidate = get_object_or_404(Candidate, pk=pk)
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)

    def put(self, request, pk):
        candidate = get_object_or_404(Candidate, pk=pk)
        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        candidate = get_object_or_404(Candidate, pk=pk)
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# API for Candidate Skills
class CandidateSkillListAPIView(APIView):
    def get(self, request):
        skills = CandidateSkill.objects.all()
        serializer = CandidateSkillSerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CandidateSkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)