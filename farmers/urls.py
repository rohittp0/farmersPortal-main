from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='farmers_index'),
    path('profile/', views.profile, name='farmers_index'),
    path('register/', views.FarmersRegisterViews, name='farmer_registration'),
    path('announcements/', views.FarmersAnnouncementsPage,
         name='farmers_announcements'),
    path('employee-list/', views.EmployeeListPage, name='employee_list'),
    path('hiring-employee/<str:email>/',
         views.HiringEmployeePage, name='hiring_employee'),
    path('hiring-request-list/', views.HiringRequestList,
         name='farmers_hiring_request_list'),
    path('delete-hiring_request/<int:id>/',
         views.DeleteHiredUser, name='delete_hiring_request'),
    path('weather-reports/', views.FarmersWeatherReportPage,
         name='farmers_weather_reports'),
    path('add-farmer-crop-details', views.FarmerCropDetailsPage,
         name='add_farmer_crop_details'),
    path('crop-list/', views.FarmerCropListPage, name='crop_list'),
    path('update/<int:id>', views.FarmerCropDetailsPage,
         name='farmers_crop_update'),
    path('delete/<int:id>/', views.FarmerCropDelete, name='farmers_crop_delete'),
]
