from django.urls import path
from companydetails.views import (CompanyEmployeeListView, CompanyEmployeeDetailView, CandidateListView,
                   CandidateDetailAPIView, CandidateSkillListAPIView)

urlpatterns = [
    path('employees/', CompanyEmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', CompanyEmployeeDetailView.as_view(), name='employee-details'),
    
    path('candidate/', CandidateListView.as_view(), name='candidate-list'),
    path('candidate/<int:pk>/', CandidateDetailAPIView.as_view(), name='candidate-details'),
    
    path('candidate/skills/', CandidateSkillListAPIView.as_view(), name='candidate-skills')
    
]

