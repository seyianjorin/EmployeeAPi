from django.urls import path

from api.views import EmployeeList, EmployeeDetail

urlpatterns = [
    path('employee/', EmployeeList.as_view()),
    path('employee/<int:pk>/', EmployeeDetail.as_view()),
]

