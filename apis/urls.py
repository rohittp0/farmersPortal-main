
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='api_index'),
    path('users', views.get_all_users, name='api_users'),
    path('users/<int:id>',
         views.get_users_detailed, name='api_get_users_detailed'),
    path('announcements', views.get_all_announcements, name='api_announcements'),
    path('weather', views.get_all_weather, name='api_weather'),
    path('crops', views.get_all_crops, name='api_crops'),
    path('hearing', views.get_all_hearing, name='api_hearing'),
    path('farmer-crop-details', views.get_all_farmer_crop_details,
         name='api_farmer_crop_details'),
]
