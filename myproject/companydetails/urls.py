from django.urls import path
from companydetails.views import (CompanyEmployeeListView, CompanyEmployeeDetailView, CandidateListView,
                                  AccessEmployeeListView,CandidateDetailAPIView, CandidateSkillListAPIView, HRAssignedCandidateListView)

urlpatterns = [
    path('employees/', CompanyEmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', CompanyEmployeeDetailView.as_view(), name='employee-details'),

    path('employees/roles/', AccessEmployeeListView.as_view(), name='employees-role'),

    path('candidates/', CandidateListView.as_view(), name='candidate-list'),
    path('candidates/<int:pk>/', CandidateDetailAPIView.as_view(), name='candidate-details'),

    path('candidate/skills/', CandidateSkillListAPIView.as_view(), name='candidate-skills'),
    path('hr-assigned-candidates/', HRAssignedCandidateListView.as_view(), name='hr-assigned-candidates'),
]

