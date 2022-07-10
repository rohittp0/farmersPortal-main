from django.conf import settings
from django.db import models
from accounts.models import User

from admins.models import Crop


class FarmerCropDetails(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    land_per_hectare = models.IntegerField('Land per hectare', default=0)
    crop_category = models.ForeignKey(Crop, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.crop_category}-{self.user.username}"


class HiringRequest(models.Model):
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)
    accepted = models.BooleanField(blank=True, null=True)
    rejected = models.BooleanField(blank=True, null=True)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    day = models.IntegerField(default=10)
    salary = models.FloatField(default=1000, help_text="per day")
    applications = models.ManyToManyField(User, related_name="applicants")
    hired_list = models.ManyToManyField(User, related_name="hired")
    declined = models.ManyToManyField(User, related_name="rejected")
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}: {self.user.first_name} {self.user.last_name} "

    @property
    def total_count(self):
        return self.applications.all().count() + self.hired_count

    @property
    def hired_count(self):
        return self.hired_list.all().count()

    @property
    def total_expenditure(self):
        return self.salary * self.day * self.hired_count

    @property
    def application_count(self):
        return self.applications.all().count() + s
