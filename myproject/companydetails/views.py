#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from itertools import cycle

from companydetails.models import CompanyEmployee, Candidate, CandidateSkill, AccessEmployee

from companydetails.serializers import (CompanyEmployeeSerializer, CandidateSkillSerializer,AccessEmployeeSerializer,
                                        CandidateSerializer, HRAssignedCandidateSerializer,)

hr_iterator = None

def get_next_hr():
    """Fetch the next HR employee in a round-robin manner."""
    global hr_iterator
    hr_queryset = AccessEmployee.objects.filter(role='HR').values_list('employee_id', flat=True)

    if not hr_queryset.exists():
        return None  # No HRs available

    if hr_iterator is None or not hr_queryset:
        hr_iterator = cycle(hr_queryset)

    return next(hr_iterator, None)

class CompanyEmployeeListView(APIView):
    def get(self, request):
        employees = CompanyEmployee.objects.all()
        serializer = CompanyEmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanyEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()

            # ✅ Automatically assign "HR" role if no role is set
            if not AccessEmployee.objects.filter(employee=employee).exists():
                AccessEmployee.objects.create(employee=employee, role="HR")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

class AccessEmployeeListView(APIView):
    def get(self, request):
        access_entries = AccessEmployee.objects.all()
        serializer = AccessEmployeeSerializer(access_entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccessEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CandidateListView(APIView):
    def get(self, request):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)
    
    def post(self, request):  
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            candidate = serializer.save()
            hr_id = get_next_hr()  # Get next available HR ID

            if hr_id:
                candidate.assigned_hr = CompanyEmployee.objects.get(id=hr_id)
                candidate.save()

            return Response(CandidateSerializer(candidate).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class HRAssignedCandidateListView(APIView):
    def get(self, request):
        hr_list = CompanyEmployee.objects.filter(accessemployee__role="HR")
        hr_data = []

        for hr in hr_list:
            assigned_candidates = Candidate.objects.filter(assigned_hr=hr)
            hr_data.append({
                "HR": hr.username,
                "Candidates": CandidateSerializer(assigned_candidates, many=True).data
            })

        return Response(hr_data, status=status.HTTP_200_OK)
