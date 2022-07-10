from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='farmers_index'),
    path('create/', views.create, name='farmers_create_job'),
    path('profile/', views.profile, name='farmers_index'),
    path('register/', views.FarmersRegisterViews, name='farmer_registration'),
    path('job/<int:id>', views.employee_hire,
         name='farmers_crop_update'),
]
