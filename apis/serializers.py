from rest_framework import serializers
from accounts.models import User
from admins.models import Announcements, Crop, Weather
from employees.models import Hearing
from farmers.models import FarmerCropDetails


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class AnnouncementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = ('__all__')


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('__all__')


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ('__all__')


class HearingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hearing
        fields = ('__all__')


class FarmerCropDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerCropDetails
        fields = ('__all__')
