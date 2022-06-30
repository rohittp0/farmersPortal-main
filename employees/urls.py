
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='employees_index'),
    path('register/', views.EmployeesRegisterViews, name='employee_registration'),
    path('hiring-request-list/', views.HiringRequestList,
         name='employee_hiring_request_list'),
    path('accepted-hiring-request/<int:id>/',
         views.AcceptedJob, name='accepted_hiring_request'),
    path('rejected-hiring_request_list/<int:id>/',
         views.RejectedJob, name='rejected_hiring_request'),

]
