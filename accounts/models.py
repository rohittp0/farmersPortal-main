from django.db import models
from django.contrib.auth.models import AbstractUser


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

    def __str__(self):
        return self.email
