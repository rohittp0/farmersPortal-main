from django.db import models
from django.contrib.auth.models import AbstractUser

from admins.models import Crop


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_employee = models.BooleanField('Is employee', default=False)
    is_farmer = models.BooleanField('Is farmer', default=False)
    age = models.IntegerField('Age of user', default=0)
    phone = models.CharField(
        'User phone number', max_length=15, blank=True)
    address = models.CharField(
        'Address of user', max_length=200, blank=True)
    aadhar = models.CharField('Aadhar number of user',
                              max_length=12, blank=True)
    is_available_for_job = models.BooleanField(
        'Available for job', default=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    salary = models.CharField(max_length=50, null=True, blank=True)
    corps = models.ForeignKey(Crop, related_name="user", on_delete=models.SET_NULL, blank=True, null=True)
    hector = models.FloatField(default=0)

    @property
    def net_worth(self):
        return self.hector * self.corps.yield_per_hector * self.corps.crop_price

    def __str__(self):
        return self.email
