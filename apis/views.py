from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import User
from admins.models import Announcements, Crop, Weather
from apis.serializers import AnnouncementsSerializer, CropSerializer, FarmerCropDetailsSerializer, UserSerializer, WeatherSerializer
from employees.models import Hearing
from farmers.models import FarmerCropDetails


@api_view(['GET'])
def index(request):
    api_urls = {
        'Get ALL Users': 'api/users/',
        'Get Users Data Detailed': 'api/users/<int:id>',
        'Get ALL Announcements': 'api/announcements/',
        'Get ALL Weather': 'api/weather/',
        'Get ALL Crops': 'api/crops/',
        'Get ALL Hearing': 'api/hearing/',
        'Get ALL Farmer Crop Details': 'api/farmer-crop-details/',
    }
    return Response({'message': 'Django REST API', 'api_urls': api_urls})


@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_users_detailed(request, id):
    response = []
    user = User.objects.filter(pk=1)
    serializer_user = UserSerializer(user, many=True)
    response.append(serializer_user.data[0])
    farmerCropDetails = FarmerCropDetails.objects.filter(user=id)
    serializer_farmerCropDetails = FarmerCropDetailsSerializer(
        farmerCropDetails, many=True)
    crops = []
    for crop in serializer_farmerCropDetails.data:
        crop_data = {}
        crop_id = crop['crop_category']
        crops_data = Crop.objects.filter(pk=crop_id)
        serializer = CropSerializer(crops_data, many=True)
        crops_data = {
            'crop_name': serializer.data[0]['crop_name'],
            'crop_price': serializer.data[0]['crop_price'],
            'crop_description': serializer.data[0]['crop_description'],
        }
        crop_data['crop_category'] = crops_data
        crop_data['land_per_hectare'] = crop['land_per_hectare']
        crops.append(crop_data)
    response.append(crops)
    return Response(response)

    return Response({'user': serializer_user.data, 'crops': serializer_farmerCropDetails.data})


@api_view(['GET'])
def get_all_announcements(request):
    announcements = Announcements.objects.all()
    serializer = AnnouncementsSerializer(announcements, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_weather(request):
    weather = Weather.objects.all()
    serializer = WeatherSerializer(weather, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_crops(request):
    crops = Crop.objects.all()
    serializer = CropSerializer(crops, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_hearing(request):
    hearing = Hearing.objects.all()
    serializer = CropSerializer(hearing, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_farmer_crop_details(request):
    farmerCropDetails = FarmerCropDetails.objects.all()
    serializer = FarmerCropDetailsSerializer(farmerCropDetails, many=True)
    return Response(serializer.data)
