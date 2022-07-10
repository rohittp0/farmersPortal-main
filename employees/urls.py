from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='employees_index'),
    path('register/', views.EmployeesRegisterViews, name='employee_registration'),
    path('accept/',
         views.accepted_job, name='accepted_hiring_request'),
    path('reject/',
         views.rejected_job, name='rejected_hiring_request'),
    path("profile/", views.profile, name="profile")
]
