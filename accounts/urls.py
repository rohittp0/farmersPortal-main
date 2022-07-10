from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_login, name='index'),
    path('logout/', views.logout, name='logout'),
]
